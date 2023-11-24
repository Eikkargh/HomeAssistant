import tinytuya
import json
from datetime import datetime

deviceID = "bfbaaae177bd6df76bttgt"
Region="eu"
Key="rhykfj4u3cv4vu5vfrwy"
Secret="fb54c68d435d49588a61f929a37c8ce3"

dt = datetime.now()
nowTime = int(datetime.timestamp(dt) * 1000)
startTime = nowTime - nowTime % 86400000
oldTime = startTime - 86400000
endTime = startTime + 86400000

logTime = 0
recordNum = 0
pFlag = True


def getCloud(xdeviceID,xstart,xend):
    c = tinytuya.Cloud(
        apiRegion=Region, 
        apiKey=Key, 
        apiSecret=Secret, 
        apiDeviceID=xdeviceID)
    r = c.getdevicelog(
        deviceid=xdeviceID,
        start=xstart,
        end=xend,
        size=20,
        evtype=7)
    return r

def processLog(fullLog):
    global logTime, recordNum
    log = fullLog['result']['logs']
    for i in log:
        if i['code'] == "record":
            value = int(i['value'])
            EventTime = i['event_time']
            if EventTime > logTime: logTime = EventTime
            if pFlag: recordNum += value
            
def getLogs():
    global pFlag
    fullLog = getCloud(deviceID, startTime, endTime)
    processLog(fullLog)
    if recordNum == 0:
        pFlag = False
        fullLog = getCloud(deviceID, oldTime, startTime)
        processLog(fullLog)
    jsonTemplate = '{"records":0,"date":"","lastTime":""}'
    jsonResult = json.loads(jsonTemplate)
    jsonResult['records'] = recordNum
    if pFlag: jsonResult['date'] = int(startTime / 1000)
    else: jsonResult['date'] = int(oldTime / 1000)
    jsonResult['lastTime'] = int(logTime / 1000)
    petJson = json.dumps(jsonResult, indent=2)
    print(petJson)


getLogs()
