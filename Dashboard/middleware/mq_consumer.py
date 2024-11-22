import stomp
import time
import sys
import xml.etree.ElementTree as ET

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, frame):
        print('Error: "%s"' % frame.body)

    def on_message(self, frame):
        print('Received a message:')
        try:
            # Parse the XML content
            root = ET.fromstring(frame.body)
            print(f"Root element: {root.tag}")
            for child in root:
                print(f"  {child.tag}: {child.text}")
        except ET.ParseError:
            print("Received message is not valid XML:")
        print(frame.body)
        print('----')

def consume_from_queue(queue_name):
    # ActiveMQ connection details
    host = "localhost"
    port = 61616
    username = "admin"
    password = "admin"

    # Create a connection
    conn = stomp.Connection([(host, port)])

    # Set up the connection
    listener = MyListener(conn)
    conn.set_listener('', listener)
    conn.connect(username, password, wait=True)

    # Subscribe to the queue
    conn.subscribe(destination=f"/queue/{queue_name}", id=1, ack='auto')

    print(f"Listening for messages on {queue_name}. Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        conn.disconnect()

if __name__ == "__main__":
    # if len(sys.argv) != 2:
        # print("Usage: python consumer_script.py <queue_name>")
        # sys.exit(1)

    queue_name = "KOLA.APP.BRIDGEINFO.IN"
    consume_from_queue(queue_name)