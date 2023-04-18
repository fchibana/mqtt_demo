import paho.mqtt.client as mqtt

# Define MQTT broker settings
# broker_address = "test.mosquitto.org"
broker_address = "localhost"
broker_port = 1883
client_id = "python-hello-world"

# Define callback function for when client connects to MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

# Create MQTT client object
client = mqtt.Client(client_id=client_id)

# Set callback function for when client connects to MQTT broker
client.on_connect = on_connect

# Connect to MQTT broker
client.connect(broker_address, broker_port)

# Publish "Hello, world!" message to topic "test/hello"
client.publish("/test/hello", "Hello, world!")

# Disconnect from MQTT broker
client.disconnect()
