# REMOTE CLAPPER

WAKE YOUR FRIEND UP WITH A CLAP

UPLOAD RecieveClapMessageMQTT.ino TO YOUR WIFI ENABLED ARDUINO.  ADD YOUR NETWORK DETAILS IN ARDUINO_SECRETS.H. ADD THE IP ADDRESS OF YOUR REMOTE SERVER RUNNING MOSQUITTO IN THE ARDUINO CODE.  

RUN detectClap.py AND CLAP IN ORDER TO SEND A MESSAGE TO A SEPARATE SUBSCRIBER.  

### Mosquitto Installation
After obtaining a server on your cloud provider of choice, enable Incoming TCP requests and then run these commands to install the Mosquitto MQTT Broker.

`sudo apt-get install mosquitto mosquitto-clients`


`sudo /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf` 


