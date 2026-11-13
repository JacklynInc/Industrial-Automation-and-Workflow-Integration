import pyads
import paho.mqtt.client as mqtt
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

# TwinCAT PLC settings
AMS_NET_ID = os.getenv("AMS_NET_ID")
ADS_PORT = int(os.getenv("ADS_PORT", "851"))

# MQTT settings
BROKER = os.getenv("BROKER")
PORT = int(os.getenv("PORT", "8883"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

# MQTT connection settings
CA_CERT = "emqxsl-ca.crt"
TOPIC = "factory/Machine1/fault"

plc = pyads.Connection(AMS_NET_ID, ADS_PORT)
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id = "projectA_fault_response"
)

client.username_pw_set(USERNAME, PASSWORD)

def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"MQTT connection result: {reason_code}")
    if reason_code==0:
        print("MQTT connection successful")
    else:
        print(f"MQTT connection rejected: {reason_code}")    

client.on_connect = on_connect

try: 
    #Connect to the PLC and MQTT broker
    plc.open()
    client.tls_set(ca_certs=CA_CERT)
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    for _ in range(50):
        if client.is_connected():
            break
        time.sleep(0.2)
    if not client.is_connected():
        raise Exception("MQTT connection was not established.")

    time.sleep(2)
    print ("MQTT connected:", client.is_connected())  
    
    previous_fault = None
    print("Monitoring PLC faults and publishing changes...")

    #Read the real PLC fault signal
    while True:    
        fault_event = plc.read_by_name(
            "GVL_Machine.bFaultEvent",
            pyads.PLCTYPE_BOOL
        )

        # Build and publish the event
        if fault_event!= previous_fault:
            message = {
                "machine" : "Machine1",
                "fault" : fault_event
            }

            info = client.publish(
                TOPIC, json.dumps(message),
                qos = 1
            )

            info.wait_for_publish (timeout=5)
            if info.is_published():
                print(f"Published: {message}")
            else:
                print("Message publication not confirmed.")

            previous_fault = fault_event
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")

except Exception as error:
        print(f"Error: {error}")

finally:
    client.loop_stop()
    client.disconnect()

    if plc.is_open:
        plc.close()