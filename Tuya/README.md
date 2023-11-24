# Tuya-Cloud-API-device-logs

The script <a href=./tuya_py_api.py>tuya_py_api.py</a> is used to fetch the logs from a smart pet feeder that runs on Tuya/ Smart Life. 
Home Assistant then uses this in a command line sensor to display the data from the logs.
<br><br>
<h1>Setup</h1>
<h2>1. Tuya Cloud API Account</h2>
<ul>
  <li>First you will need to have the device added to either the Tuya or Smart Life app.</li>
  <li>Set a username and password in the app if you have not done so already. </li>
  <li>Create a <a href=https://auth.tuya.com/>Tuya Cloud API</a> account. </li>
  <li>Then follow the <a href=./Tuya.IoT.API.Setup.v2.pdf>PDF Instructions</a>.</li>
</ul><br>
<h2>2. Tuya Python API</h2>
To access the Tuya API I use <a href=https://github.com/jasonacox/tinytuya>tinytuya</a> from <a href=https://github.com/jasonacox/>@jasonacox</a>.<br>
I recommend checking it out for the many other things this API can do not mentioned here.
<ul>
  <li>To install, use command within the environment used. In my case a Home Asssistant docker container:<br>
    <code>python3 -m pip install tinytuya</code></li>
</ul><br>
<h1>Home Assistant</h1>
<h2>3. Python Script</h2>
<ul>
  <li>Add the script <a href=./tuya_py_api.py>tuya_py_api.py</a> to your /config/pyscript folder.</li>
  <li>Update the script variables with values from your Tuya Cloud API account.<br>
    <pre><code>
      deviceID = "DEVICE_ID"     # either from Tuya cloud or tinytuya scan.
      region = "REGION_LETTERS"  # (cn, us, us-e, eu, eu-w, or in) depending on what you picked during 1.
      key = "CLIENT_ID"          # from Tuya Cloud Authorisation
      secret = "API_SECRET"      # from Tuya Cloud Authorisation
    </code></pre></li>
    <li>The script produces a JSON output:<br>
    <pre><code>
 {
  "records": 3,             #number of times the pet feeder has been triggered
  "date": 1700784000,       #Unix timestamp of the record date
  "lastTime": 1700831203    #Unix timestamp of last feed
}
    </code></pre>
    </li>
</ul>
<h2>4. configuration.yaml</h2>
<ul>
  <li>Example Home Assistant config can be found at <a href="./configuration.yaml">configuration.yaml</li>
  <li>The command_line sensor triggers the python script, recieves a JSON string and split this into attributes ready to template.<br>
  <pre><code>
sensor:
  ##Other sensors##
  # Tuya Pet Feeder Record sensor
  - platform: command_line
    name: 'Pet Feeder - Record'
    unique_id: tuya_pet_record
    scan_interval: 300
    command_timeout: 30
    command: python3 ./pyscript/tuya_py_api.py
    value_template: '{{ value_json }}'
    json_attributes:
      - records
      - date
      - lastTime
  </code></pre></li>
  <li>The code under <code>template:</code> shows examples of sensors that can be used in your lovelace dashboard </li>  
</ul>
<h2>5. lovelace.yaml</h2>
More example code but this time for the dashboard itself resulting. <br>
This example uses sensors from the official <a href=https://www.home-assistant.io/integrations/tuya/>Tuya Integration</a>.<br>
<img src=./pet_feeder.jpg>

