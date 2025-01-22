from flask import Flask, render_template, request, jsonify
import markdown
import os
import argparse
import webbrowser
from threading import Timer
import requests
from urllib.parse import quote, unquote
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Dictionary to store file mappings and observers
file_mappings = {}
file_observers = {}

# Add WebSocket support to the HTML template
TEMPLATE_CONTENT = '''
<!DOCTYPE html>
<html>
<head>
    <title>Markdown Viewer</title>
    <!-- Mermaid Support -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <!-- Code Highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism-okaidia.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-bash.min.js"></script>
    <!-- Socket.IO -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script>
        // Initialize Mermaid
        mermaid.initialize({ 
            startOnLoad: true,
            theme: 'default'
        });

        // Initialize Socket.IO
        let socket = null;
        
        function initializeSocket() {
            console.log('Initializing Socket.IO connection...');
            
            socket = io.connect('http://localhost:' + window.location.port, {
                transports: ['websocket'],
                reconnection: true,
                reconnectionAttempts: 5
            });

            const currentPath = window.location.pathname;
            
            socket.on('connect', () => {
                console.log('Successfully connected to WebSocket server');
            });

            socket.on('connect_error', (error) => {
                console.error('WebSocket connection error:', error);
            });

            socket.on('disconnect', () => {
                console.log('Disconnected from WebSocket server');
            });
            
            socket.on('file_changed', (data) => {
                console.log('Received file_changed event:', data);
                console.log('Current path:', currentPath);
                
                if (data.path === currentPath) {
                    console.log('File changed, reloading content...');
                    window.location.reload();
                }
            });
        }

        // Initialize socket when DOM is ready
        document.addEventListener('DOMContentLoaded', () => {
            console.log('DOM loaded, initializing WebSocket...');
            initializeSocket();
        });
    </script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        pre {
            background-color: #272822;
            border-radius: 4px;
            padding: 1em;
            margin: .5em 0;
            overflow: auto;
        }
        code {
            font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
            font-size: 1em;
            line-height: 1.5;
        }
        pre code {
            color: #f8f8f2;
        }
        .mermaid {
            margin: 20px 0;
            text-align: center;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        blockquote {
            border-left: 4px solid #ddd;
            margin: 0;
            padding-left: 20px;
            color: #666;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f6f8fa;
        }
    </style>
</head>
<body>
    {{ content|safe }}
</body>
</html>
'''

def setup_template():
    """Create templates directory and markdown template."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(script_dir, 'templates')
    os.makedirs(template_dir, exist_ok=True)
    template_path = os.path.join(template_dir, 'markdown.html')
    with open(template_path, 'w') as f:
        f.write(TEMPLATE_CONTENT)

class MarkdownFileHandler(FileSystemEventHandler):
    def __init__(self, file_path, app_context):
        self.file_path = file_path
        self.app_context = app_context

    def on_modified(self, event):
        if event.src_path == self.file_path:
            with self.app_context:
                print(f"File changed: {self.file_path}")
                path = f'/view/{normalize_path(os.path.dirname(self.file_path))}/{os.path.basename(self.file_path)}'
                print(f"Emitting file_changed event with path: {path}")
                # Simple emit without broadcast parameter
                socketio.emit('file_changed', {'path': path})

def setup_file_watcher(target_dir, filename):
    """Set up a file watcher for the specified markdown file."""
    file_path = get_file_path(target_dir, filename)
    
    # Create an observer and event handler
    observer = Observer()
    event_handler = MarkdownFileHandler(file_path, app.app_context())
    
    # Schedule watching the directory containing the file
    observer.schedule(event_handler, os.path.dirname(file_path), recursive=False)
    observer.start()
    
    # Store the observer for cleanup
    file_observers[file_path] = observer
    print(f"Started watching: {file_path}")

def cleanup_file_watcher(target_dir, filename):
    """Clean up the file watcher for the specified markdown file."""
    file_path = get_file_path(target_dir, filename)
    if file_path in file_observers:
        file_observers[file_path].stop()
        file_observers[file_path].join()
        del file_observers[file_path]
        print(f"Stopped watching: {file_path}")

def normalize_path(path):
    """Convert path to Unix format with forward slashes."""
    abs_path = os.path.abspath(path)
    normalized = abs_path.replace('\\', '/')
    # Convert Windows drive letter to lowercase and remove colon
    if len(normalized) >= 2 and normalized[1] == ':':
        normalized = normalized[0].lower() + normalized[2:]
    return normalized.rstrip('/')

def get_file_path(target_dir, filename):
    """Get the full file path for reading."""
    # Add back the drive letter colon for file operations
    if len(target_dir) >= 1 and not ':' in target_dir:
        full_path = target_dir[0] + ':' + target_dir[1:]
    else:
        full_path = target_dir
    return os.path.join(full_path, filename)

def is_port_in_use(port):
    """Check if the given port is already in use."""
    try:
        requests.get(f'http://localhost:{port}/', timeout=1)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

def register_file_with_server(port, target_dir, filename):
    """Register a new file with an existing server."""
    try:
        print(f"Registering {filename} from {target_dir}")
        response = requests.post(
            f'http://localhost:{port}/register',
            json={'work_dir': target_dir, 'filename': filename},
            timeout=1
        )
        return response.status_code == 200
    except (requests.ConnectionError, requests.Timeout):
        return False

def process_code_blocks(content):
    """Process code blocks to add syntax highlighting and handle Mermaid diagrams."""
    def replace_code_block(match):
        full_block = match.group(0)
        language = match.group(1) if match.group(1) else ''
        code = match.group(2)
        
        if language.lower() == 'mermaid':
            return f'<div class="mermaid">\n{code}\n</div>'
        else:
            language_class = f'language-{language}' if language else ''
            return f'<pre><code class="{language_class}">{code}</code></pre>'
    
    # Replace code blocks with proper HTML
    pattern = r'```(\w*)\n(.*?)```'
    return re.sub(pattern, replace_code_block, content, flags=re.DOTALL)

def read_md_file(target_dir, filename):
    """Read and process markdown file content."""
    file_path = get_file_path(target_dir, filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Process code blocks (including Mermaid) before Markdown conversion
        content = process_code_blocks(content)
        
        # Convert remaining Markdown to HTML
        md = markdown.Markdown(extensions=['extra', 'codehilite'])
        html_content = md.convert(content)
        
        return html_content
            
    except FileNotFoundError:
        return f"<p>Error: Could not find file {file_path}</p>"
    except Exception as e:
        return f"<p>Error reading file: {str(e)}</p>"

def open_browser_for_file(port, target_dir, filename):
    """Open browser with the markdown URL."""
    path = f"{target_dir}/{filename}"
    webbrowser.open(f'http://localhost:{port}/view/{path}')

@app.route('/view/<path:full_path>')
def render_markdown(full_path):
    """Endpoint for rendering markdown content."""
    print(f"Requested path: {full_path}")
    print(f"Available mappings: {file_mappings}")
    
    if full_path in file_mappings:
        target_dir, md_file = file_mappings[full_path]
        content = read_md_file(target_dir, md_file)
        return render_template('markdown.html', content=content)
    return f"<p>Error: Path {full_path} not found</p>"

@app.route('/register', methods=['POST'])
def register_file_endpoint():
    """Endpoint for registering new files."""
    data = request.json
    work_dir = normalize_path(data['work_dir'])
    path = f"{work_dir}/{data['filename']}"
    file_mappings[path] = (work_dir, data['filename'])
    setup_file_watcher(work_dir, data['filename'])
    print(f"Registered path: {path}")
    return jsonify({"status": "success"})

def main():
    """Main function to handle command line arguments and start server."""
    parser = argparse.ArgumentParser(description='Render Markdown files with support for code highlighting, Mermaid diagrams, and live reload')
    parser.add_argument('target_directory', help='Target directory containing the markdown file')
    parser.add_argument('markdown_filename', help='Name of the markdown file to render')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on (default: 5000)')
    
    args = parser.parse_args()
    
    # Setup template
    setup_template()
    
    # Normalize target directory path
    target_dir = normalize_path(args.target_directory)
    print(f"Target directory: {target_dir}")
    
    # Check if server is already running
    server_exists = is_port_in_use(args.port)
    print(f"Server status: {'running' if server_exists else 'not running'}")
    
    if server_exists:
        print(f"Server already running on port {args.port}")
        if register_file_with_server(args.port, target_dir, args.markdown_filename):
            print(f"Registered {args.markdown_filename}")
            open_browser_for_file(args.port, target_dir, args.markdown_filename)
        else:
            print("Failed to register file with server")
    else:
        print(f"Starting new server on port {args.port}")
        # Register first file
        path = f"{target_dir}/{args.markdown_filename}"
        file_mappings[path] = (target_dir, args.markdown_filename)
        setup_file_watcher(target_dir, args.markdown_filename)
        
        # Open browser after server starts
        Timer(1.5, lambda: open_browser_for_file(args.port, target_dir, args.markdown_filename)).start()
        
        # Start server with Socket.IO support
        socketio.run(app, host='127.0.0.1', debug=False, port=args.port)

if __name__ == '__main__':
    try:
        main()
    finally:
        # Clean up all file watchers
        for target_dir, filename in file_mappings.values():
            cleanup_file_watcher(target_dir, filename)