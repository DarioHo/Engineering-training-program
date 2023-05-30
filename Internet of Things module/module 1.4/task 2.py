import paho.mqtt.publish as publish

hostname = "test.mosquitto.org"
port = 1883

topic = "PC302/test" 

publish.single(topic, payload="Nice to meet you, MQTT:)!", qos=0,
	hostname=hostname,
	port=port)
