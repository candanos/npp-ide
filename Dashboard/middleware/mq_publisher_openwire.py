import jpype
import jpype.imports
from jpype.types import *
import sys
import os

# Path to ActiveMQ client JAR file
activemq_jar = r'C:\java\middleware\activemq-client-6.1.3.jar'
activemq_jar = r'C:\java\middleware\apache-activemq-6.1.3\activemq-all-6.1.3.jar'

# Path to Java 17 installation
java_home = r'C:\java\jdk-17.0.9'
# Path to JAR files
jar_dir = r'C:\java\middleware'
dep1 = os.path.join(jar_dir, "log4j-api-2.24.1.jar")
dep2 = os.path.join(jar_dir, "log4j-core-2.24.1.jar")
dep3 = os.path.join(jar_dir, "javax.jms-api-2.0.1.jar")

def set_java_environment():
    
    # Set JAVA_HOME
    os.environ['JAVA_HOME'] = java_home
    print(f"JAVA_HOME set to: {java_home}")
    
    # Extend PATH
    java_bin = os.path.join(java_home, 'bin')
    os.environ['PATH'] = f"{java_bin}{os.pathsep}{os.environ['PATH']}"

    
def send_xml_to_queue(xml_file_path, queue_name):
    set_java_environment()
    if not jpype.isJVMStarted():
        classpath = [activemq_jar, dep1, dep2, dep3]
        jpype.startJVM(classpath=classpath)

    try:
        # Import Java classes
        ConnectionFactory = jpype.JClass("org.apache.activemq.ActiveMQConnectionFactory")
        Session = jpype.JClass("javax.jms.Session")
        TextMessage = jpype.JClass("javax.jms.TextMessage")

        # Set up the connection
        factory = ConnectionFactory("tcp://localhost:61616")
        connection = factory.createConnection()
        session = connection.createSession(False, Session.AUTO_ACKNOWLEDGE)

        # Create a queue and producer
        queue = session.createQueue(queue_name)
        producer = session.createProducer(queue)

        # Read the XML file
        with open(xml_file_path, 'r') as file:
            xml_content = file.read()

        # Create and send the message
        text_message = session.createTextMessage(xml_content)
        producer.send(text_message)

        print(f"XML file sent to {queue_name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close resources
        if 'session' in locals():
            session.close()
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    # if len(sys.argv) != 3:
        # print("Usage: python script.py <xml_file_path> <queue_name>")
        # sys.exit(1)
                        
    xml_file_path = r'C:\github\kola-cli\tests\cadrel\dirs\segotl5798\app\t613vcom\send_to_kola_files\EXTERNAL_88853474.DRW-077004_20241015195118.xml'
    queue_name = "KOLA.APP.BRIDGEINFO.IN"
    send_xml_to_queue(xml_file_path, queue_name)