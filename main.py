# FIXED IMPORTS
import paho.mqtt.client as mqtt
from time import sleep

username = 'anom'

def on_connect(client, userdata, flags, rc):
    global username
    client.subscribe("Your MQTT Channel")

    if rc == 0:
        print("Connected Successfully with result code " + str(rc))
    else:
        print("Error occured with result code" + str(rc))

    username = input('Type your name: ')


def on_message(client, userdata, msg):
    content = msg.payload.decode()
    print("Channel " + str(msg.topic) + " says: " + content)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect_async("Your MQTT Server", 1883, 60)
client.loop_start()

sleep(1)
while True:
    sleep(0.5)
    message = input("Type your message: ")
    client.publish("Your MQTT Channel", payload=message, qos=0, retain=False)
            
client.loop_forever()