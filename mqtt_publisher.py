import paho.mqtt.client as mqtt

# Define the broker and topic
broker = "broker.hivemq.com"  # Public broker for testing
topic = "home/livingroom/temperature"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker, 1883, 60)

# Publish a message
client.publish(topic, "22.5")  # Publishing temperature as 22.5 degrees

# Disconnect
client.disconnect()
