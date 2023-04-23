# ewpe-mqtt-smart

Works with: Lexent Mevagissey 16L Dehumidifier

Uses: 
- [ewpe-smart-mqtt](https://github.com/stas-demydiuk/ewpe-smart-mqtt) node created by [stas-demydiuk](https://github.com/stas-demydiuk)
- Home Assistant
- EWPE Smart - Android app
- Local Mosquitto MQTT Broker


##Instructions

1. Check for/install node
``` 
node --version
npm install
```
2. Clone ewpe-smart-mqtt
```
git clone https://github.com/stas-demydiuk/ewpe-smart-mqtt
```
3. Change device_manager.js statusKey to match device. For me this was:
```
const statusKeys = [
    'Pow', 'Dwet', 'DwatSen', 'Dmod', 'WdSpd', 'Dfltr', 'DwatFul',
    'AllErr', 'TemSen', 'Health', 'AppTimer'
]
```
4. If you are wanting to launch this as a service
```
sudo mv ewpe-smart-mqtt /opt/.
sudo nano /etc/systemd/system/ewpe-smart-mqtt.service
```
```
[Service]
ExecStart=/usr/bin/node /opt/ewpe-smart-mqtt/index.js --NETWORK="192.168.1.255" --MQTT_SERVER="mqtt://127.0.0.1" --MQTT_PORT="1883" --MQTT_USERNAME="" --MQTT_PASSWORD="" --MQTT_BASE_TOPIC="ewpe-smart" --DEVICE_POLL_INTERVAL="5000" 
# Required on some systems
WorkingDirectory=/opt/ewpe-smart-mqtt
StandardOutput=inherit
StandardError=inherit
Restart=always
RestartSec=10
User=pi
Group=pi
[Install]
WantedBy=multi-user.target
```
5. Start the service
```
sysudo systemctl enable ewpe-smart-mqtt.service
sudo systemctl start ewpe-smart-mqtt.service
```
