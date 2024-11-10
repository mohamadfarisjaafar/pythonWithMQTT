import paho.mqtt.client as mqtt

# Define the broker and topic
broker = "broker.hivemq.com"  # Public broker for testing
topic = "home/livingroom/temperature"

# Callback when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Create an MQTT client instance
client = mqtt.Client()
client.on_message = on_message

# Connect to the broker and subscribe to the topic
client.connect(broker, 1883, 60)
client.subscribe(topic)

# Loop forever to maintain connection
client.loop_forever()
