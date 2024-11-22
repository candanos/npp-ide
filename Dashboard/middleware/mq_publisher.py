import stomp
import time
import sys

def send_xml_to_queue(xml_file_path, queue_name):
    # ActiveMQ connection details
    host = "localhost"
    port = 61613
    username = "admin"
    password = "admin"

    # Create a connection
    conn = stomp.Connection([(host, port)])

    # Define a listener to handle connection events
    class MyListener(stomp.ConnectionListener):
        def on_error(self, frame):
            print('Error: "%s"' % frame.body)

        def on_disconnected(self):
            print('Disconnected')

    # Set up the connection
    conn.set_listener('', MyListener())
    conn.connect(username, password, wait=True)

    try:
        # Read the XML file
        with open(xml_file_path, 'r') as file:
            xml_content = file.read()

        # Send the XML content to the queue
        conn.send(body=xml_content, destination=f"/queue/{queue_name}")
        print(f"XML file sent to {queue_name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Disconnect from ActiveMQ
        time.sleep(2)  # Give some time for the message to be sent
        conn.disconnect()

if __name__ == "__main__":
    # if len(sys.argv) != 3:
        # print("Usage: python script.py <xml_file_path> <queue_name>")
        # sys.exit(1)

    # xml_file_path = sys.argv[1]
    # queue_name = sys.argv[2]    
    xml_file_path = r'C:\github\kola-cli\tests\cadrel\dirs\send_to_kola_files\EXTERNAL_88853474.DRW-077004_20240906113005.xml'
    queue_name = "KOLA.APP.BRIDGEINFO.IN"
    send_xml_to_queue(xml_file_path, queue_name)