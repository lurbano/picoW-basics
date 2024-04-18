Note: the examples/ directory has the code for the MakerspaceNetwork demo picoW that has a light sensor (photoresistor), and LED. 

# Example Adding Buttons: PicoW

This example shows the procedure I used to have a web page to turn the picoW's onboard LED on and off.  
* create a button on the web page 
* on a click, send a message to the server
* server recieves the message and does something (get the time, or light the led on the Pico)
* server sends a message back to the webpage (client) to let it know what happened.

## Create button (html) (index.html)
Inside the ```index.html``` file's ```<body>``` tags add button code:
```html
<input type="button" id = "ledON" value="LED ON">
```
Give it a unique ```id```, and the ```value``` is what shows up on the button.

## Send message on click (JavaScript) (index.html)
Inside the ```index.html``` file's ```<script>``` tags add code to detect a click on the button and send message to server:
```js
    ledON.addEventListener("click", function(){
        sendRequest("/", "lightON");
    })
```
The first argument ("/"), indicates the base of the webpage url (does not need to change), and the second argument is the ```action``` paramenter that's sent to the server (see the protocol). A third argument would be the ```value``` parameter.

The message is sent as a POST request.

## Server Recieve Message (code.py)
The server recieves the POST message sent to "/" in the section that starts with:
```python
@server.route("/", "POST")
```

Data recieved with the right protocol (see above) will be accessible as:
```python
data['action']
data['value']
```

To turn the pico's onboard LED (assuming that the variable ```led``` is set up previously in the code) on we do:
```python
    if (data['action'] == "lightON"):
            led.value = True
            rData['item'] = "onboardLED"
            rData['status'] = led.value
```

Notice that we set the values of ```rData``` which is returned to the client (webpage) at the end of the function.

## Webpage handles the reply
The reply from the server gets caught in the ```sendRequest``` function in the ```//Handle responses``` section. The response is captured and put into the ```data``` dictionary (which is the ```rData``` dictionary that was returned from the server, renamed as 'data["item"]' and 'data["status"]'). In this example, the "status" is put into the DIV with the id "ledStatus" on the webpage with:
```js
                //Handle responses
                if (data["item"] == "onboardLED") {
                    ledStatus.innerText = data["status"];
                }
```


## Test
* Open ```code.py``` in Thonny and run.
* Click on the url link in the Thonny Shell to get the webpage
* Click the "LED ON" and "LED OFF" buttons on the page. 
    * The led on the picoW should turn on and off, and it should say "true" and "false" on the webpage.


# Example: Sending requests to other devices from the server

Import uNetComm and set it up after the server is set up (around line 30 in code.py):
```python
from uNetComm import *
comm = uNetComm(pool)
```

To send a message to ```deviceName``` use:
```python
comm.request("deviceName", "setMode", "red")
```

where the first variable is the address, while the second and third variables are the data["action"] and data["value"].
