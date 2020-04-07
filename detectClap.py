
import sounddevice as sd
import numpy as np
import time
import paho.mqtt.client as mqtt


global previous_reading
previous_reading = 0
print("Ready ")

class SoundMonitor():
    def __init__(self):
        self.previous_value = 0
        self.client = mqtt.Client()
        self.client.connect("54.204.183.201",1883,60)

    def print_sound(self, indata, outdata, frames, time, status):
        volume_norm = int(np.linalg.norm(indata)*10)

        if(volume_norm > 100 and self.previous_value < 100):
            print ("CLAP")
            self.publish_message()
        self.previous_value = volume_norm

    def publish_message(self):


        self.client.publish("topic/clap", "Hello SID!!!!");
        print("SENT MESSAGE")

sm = SoundMonitor()
with sd.Stream(callback=sm.print_sound):
    sd.sleep(100000)


