import paho.mqtt.client as mqtt

hostname = "test.mosquitto.org" # Sandbox broker
port = 1883 # Default port for unencrypted MQTT

topic = "PC302/#" 

def on_connect(client, userdata, flags, rc):

	print("Connection result: " + str(rc))
	if rc == 0:
		client.subscribe(topic)
	
def on_message(client, userdata, message):
	print("Received message on %s: %s (QoS = %s)" % (message.topic, message.payload.decode("utf-8"), str(message.qos)))

def on_disconnect(client, userdata, rc):
	if rc != 0:
		print("Disconnected unexpectedly")
		
# Initialize client instance
client = mqtt.Client()

# Bind events to functions
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to the specified broker
client.connect(hostname, port=port)

# Network loop runs in the background to listen to the events
client.loop_forever()
