import paho.mqtt.publish as publish

hostname = "test.mosquitto.org"
port = 1883

topic = "PC305/#" 
topic_state_eme = "PC305/traffic_light/emergency" 

publish.single(topic_state_eme, 1, qos=0,
	hostname=hostname,
	port=port)
