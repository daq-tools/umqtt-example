# Alias MicroPython modules.
import sys
import socket
import struct
import binascii
sys.modules["usocket"] = socket
sys.modules["ustruct"] = struct
sys.modules["ubinascii"] = binascii


from umqtt.universal import MQTTClient


def test_connect():
    mqtt = MQTTClient(client_id="umqtt_client", server="127.0.0.1")
    mqtt.connect()
    mqtt.disconnect()


def test_publish():
    mqtt = MQTTClient(client_id="umqtt_client", server="127.0.0.1")
    mqtt.connect()
    mqtt.publish("foobar", "Hello world!")
    mqtt.disconnect()
