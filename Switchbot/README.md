## Switchbot API

### Current Device
- [Strip Light](https://github.com/Eikkargh/HomeAssistant/tree/main/Switchbot/Strip%20Light)
- [Motion Sensor](https://github.com/Eikkargh/HomeAssistant/tree/main/Switchbot/Motion)
- [Temperature/ Humidity Sensor](https://github.com/Eikkargh/HomeAssistant/tree/main/Switchbot/Temp-Humidity%20Sensor)
- [Scenes](https://github.com/Eikkargh/HomeAssistant/tree/main/Switchbot/Scenes) (Also used for Switchbot IR with Hub)

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
