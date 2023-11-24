#! /usr/bin/env python
import requests
import json
import pycryptodome

#variables
nowTime = int(time.time() * 1000)
startTime = nowTime - nowTime % 86400000
endTime = startTime + 86400000
request_timeout = 10
retries = 3
retry_delay = 2
device = "bfbaaae177bd6df76bttgt"
clientId = "rhykfj4u3cv4vu5vfrwy"
accessSecret = "fb54c68d435d49588a61f929a37c8ce3"

def getSign():
    

def getUrl(xurl, xheaders):
    sign = getSign()
    urlList = ["https://openapi.tuyaeu.com/v2.0/cloud/thing/" + device,
        "/logs?codes=record&end_time=" + str(endTime),
        "&query_type=1&size=20&start_time=" + str(startTime),
        "&type=7"
        " --header 'sign_method: HMAC-SHA256'",
        " --header 'client_id: " + clientId + "'",
        " --header 't: " + str(nowTime) + "'",
        " --header 'mode: cors'",
        " --header 'Content-Type: application/json'",
        " --header 'sign: " + sign + "'",
        " --header 'access_token: " + accessSecret + "'"]
    fullUrl = ""
    for i in range(len(urlList)):
        fullUrl += url[i]
    return fullUrl

def requestLog():
    

from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
)

ACCESS_ID = "rhykfj4u3cv4vu5vfrwy"
ACCESS_KEY = "fb54c68d435d49588a61f929a37c8ce3"
API_ENDPOINT = "https://openapi.tuyaeu.com"
MQ_ENDPOINT = "wss://mqe.tuyaeu.com:8285/"

