import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime

MQTT_BROKER = "localhost"
MQTT_TOPIC = "iot/sensors/temperature"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

print("Sensor Publisher Started...")

while True:
    temperature = round(random.uniform(25.0, 45.0), 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    payload = f"{timestamp},{temperature}"
    client.publish(MQTT_TOPIC, payload)
    
    print(f"Published → {payload}")
    time.sleep(2)