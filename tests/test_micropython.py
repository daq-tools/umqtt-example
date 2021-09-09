from unittest import TestCase
from umqtt.simple import MQTTClient


class MosquittoTests(TestCase):

    def test_connect(self):
        mqtt = MQTTClient(client_id="umqtt_client", server="127.0.0.1")
        mqtt.connect()
        mqtt.disconnect()

    def test_publish(self):
        mqtt = MQTTClient(client_id="umqtt_client", server="127.0.0.1")
        mqtt.connect()
        mqtt.publish("foobar", "Hello world!")
        mqtt.disconnect()
