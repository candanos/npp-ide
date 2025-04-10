from flask import Flask, render_template, request, jsonify
import markdown
import os
import argparse
import webbrowser
from threading import Timer
import requests
from urllib.parse import quote, unquote
import re

app = Flask(__name__)

# Dictionary to store file mappings
file_mappings = {}

# HTML template with support for Markdown content, code highlighting, and Mermaid diagrams
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
    <script>
        // Initialize Mermaid
        mermaid.initialize({ 
            startOnLoad: true,
            theme: 'default'
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

def normalize_path(path):
    """Convert path to Unix format with forward slashes."""
    abs_path = os.path.abspath(path)
    normalized = abs_path.replace('\\', '/')
    # Convert Windows drive letter to lowercase but keep the colon
    if len(normalized) >= 2 and normalized[1] == ':':
        normalized = normalized[0].lower() + normalized[1:]
    return normalized.rstrip('/')

def get_file_path(target_dir, filename):
    """Get the full file path for reading."""
    return os.path.join(target_dir, filename)

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
        normalized_dir = normalize_path(target_dir)
        print(f"Registering {filename} from {normalized_dir}")
        response = requests.post(
            f'http://localhost:{port}/register',
            json={'work_dir': normalized_dir, 'filename': filename},
            timeout=1
        )
        return response.status_code == 200
    except (requests.ConnectionError, requests.Timeout):
        return False

def open_browser_for_file(port, target_dir, filename):
    """Open Firefox browser with the markdown URL."""
    normalized_dir = normalize_path(target_dir)
    encoded_path = quote(f"{normalized_dir}/{filename}")
    url = f'http://localhost:{port}/view/{encoded_path}'
    
    print(f"Opening URL: {url}")
    
    import os
    import subprocess
    import sys
    
    try:
        if sys.platform.startswith('win'):
            firefox_paths = [
                os.path.expandvars(r'%ProgramFiles%\Mozilla Firefox\firefox.exe'),
                os.path.expandvars(r'%ProgramFiles(x86)%\Mozilla Firefox\firefox.exe')
            ]
        elif sys.platform.startswith('linux'):
            firefox_paths = ['/usr/bin/firefox', '/snap/bin/firefox', '/usr/lib/firefox/firefox']
        else:
            firefox_paths = ['/Applications/Firefox.app/Contents/MacOS/firefox']
            
        for firefox_path in firefox_paths:
            if os.path.exists(firefox_path):
                subprocess.Popen([firefox_path, '-new-tab', url])
                print(f"Opened Firefox from: {firefox_path}")
                return
                
        print("Firefox executable not found, trying webbrowser module...")
        browser = webbrowser.get('firefox')
        browser.open_new_tab(url)
        
    except Exception as e:
        print(f"Error launching Firefox: {e}")
        print("Falling back to default browser")
        webbrowser.open_new_tab(url)

@app.route('/register', methods=['POST'])
def register_file_endpoint():
    """Endpoint for registering new files."""
    data = request.json
    work_dir = data['work_dir']
    filename = data['filename']
    path = f"{work_dir}/{filename}"
    
    # Store both the normalized path and the original file path
    file_mappings[path] = (work_dir, filename)
    print(f"Registered path: {path}")
    return jsonify({"status": "success"})

@app.route('/view/<path:full_path>')
def render_markdown(full_path):
    """Endpoint for rendering markdown content."""
    print(f"Requested path: {full_path}")
    decoded_path = unquote(full_path)
    print(f"Decoded path: {decoded_path}")
    print(f"Available mappings: {file_mappings}")
    
    if decoded_path in file_mappings:
        target_dir, md_file = file_mappings[decoded_path]
        content = read_md_file(target_dir, md_file)
        return render_template('markdown.html', content=content)
    
    # Try alternative path formats
    for mapped_path, (dir_path, filename) in file_mappings.items():
        if decoded_path.endswith(f"{dir_path}/{filename}"):
            content = read_md_file(dir_path, filename)
            return render_template('markdown.html', content=content)
    
    return f"<p>Error: Path {decoded_path} not found in mappings</p>"

def main():
    """Main function to handle command line arguments and start server."""
    parser = argparse.ArgumentParser(description='Render Markdown files with support for code highlighting and Mermaid diagrams')
    parser.add_argument('target_directory', help='Target directory containing the markdown file')
    parser.add_argument('markdown_filename', help='Name of the markdown file to render')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on (default: 5000)')
    
    args = parser.parse_args()
    
    setup_template()
    
    target_dir = normalize_path(args.target_directory)
    print(f"Target directory: {target_dir}")
    
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
        path = f"{target_dir}/{args.markdown_filename}"
        file_mappings[path] = (target_dir, args.markdown_filename)
        
        Timer(1.5, lambda: open_browser_for_file(args.port, target_dir, args.markdown_filename)).start()
        
        app.run(host='127.0.0.1', debug=False, port=args.port)

if __name__ == '__main__':
    main()