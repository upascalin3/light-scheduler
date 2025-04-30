# subscriber.py
import serial
import paho.mqtt.client as mqtt
from datetime import datetime
import time

# Initialize serial connection
ser = serial.Serial('COM6', 9600)  # Change to your correct COM port

# Store ON and OFF times
schedule = {"ON": None, "OFF": None}

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    now = datetime.now().strftime("%H:%M")

    if payload.startswith("ON:"):
        schedule["ON"] = payload.split(":", 1)[1]
        print(f"Received MQTT message: ON at {schedule['ON']}")
    elif payload.startswith("OFF:"):
        schedule["OFF"] = payload.split(":", 1)[1]
        print(f"Received MQTT message: OFF at {schedule['OFF']}")
    else:
        print(f"Ignored unexpected MQTT message: {payload} at {now}")

# Set up MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("relay/schedule")
client.loop_start()

# Loop to check the time and control Arduino
while True:
    now = datetime.now().strftime("%H:%M")

    if schedule["ON"] == now:
        ser.write(b'1')
        print(f"Sent to Arduino: ON at {now}")
        time.sleep(60)  # avoid triggering again within the same minute

    elif schedule["OFF"] == now:
        ser.write(b'0')
        print(f"Sent to Arduino: OFF at {now}")
        time.sleep(60)

    time.sleep(1)
