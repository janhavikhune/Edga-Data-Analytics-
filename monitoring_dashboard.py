import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_TOPIC = "iot/sensors/temperature"

def on_message(client, userdata, message):
    data = message.payload.decode()
    timestamp, temperature = data.split(",")
    temperature = float(temperature)

    print(f"Received at {timestamp} → Temp = {temperature} °C")

    if temperature > 40:
        print("ALERT: High Temperature Detected!")

client = mqtt.Client()
client.connect(MQTT_BROKER)

client.subscribe(MQTT_TOPIC)
client.on_message = on_message

print("Monitoring Dashboard Running...")
client.loop_forever()
