import paho.mqtt.client as mqtt

# Define MQTT broker settings
# broker_address = "test.mosquitto.org"
broker_address = "localhost"
broker_port = 1883
client_id = "python-subscriber"

# Define callback function for when client connects to MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    # Subscribe to "test/hello" topic
    client.subscribe("/test/hello")

# Define callback function for when message is received on subscribed topic
def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode()))

# Create MQTT client object
client = mqtt.Client(client_id=client_id)

# Set callback functions for when client connects to MQTT broker and when message is received on subscribed topic
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(broker_address, broker_port)

# Start MQTT network loop
client.loop_forever()
