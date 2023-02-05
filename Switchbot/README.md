## Switchbot API

### Current Device
- Strip Light
- Motion Sensor
- Temperature/ Humidity Sensor
- Scenes

### Steps:
1. Get API Key from mobile app developer options (press "App Version" 10 times if no developer option).
2. Using console get device list: 
```
curl -H "Authorization: <API KEY>" -H "Accept: appication/JSON" https://api.switch-bot.com/v1.0/devices
```
3. Using console get scene list:
```
curl -H "Authorization: <API KEY>" -H "Accept: appication/JSON" https://api.switch-bot.com/v1.0/scenes
```
4. Enter you API Key, deviceId or sceneId detail in your secrets.yaml and scripts.yaml for your device. 
