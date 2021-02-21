#!/usr/bin/python

import time
import requests
from gpiozero import Button
from gpiozero import LED
from phue import Bridge
from signal import pause

button = Button(2)

def ring_bell():
    bell = LED(22)
    bell.on()
    time.sleep(0.5)
    bell.off()
    
# Send Telegram Message
def telegram_bot_sendtext(bot_message):
    
    bot_token = '111111111:XXXXXXXXXXXXXXXXXXX'
    bot_chatID = '-123456789'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    try:
        response = requests.get(send_text)
        return response.json()  
    except OSError:
        pass
    return False
      

# set alert state
def set_alert_state(lights, store_settings):

    # Set brightness of lamp 1 to max, rapidly
    #b.set_light(1, 'bri', 254, transitiontime=1)

    for light in store_settings:
        lights[light].transitiontime = 1
        lights[light].on = True
        lights[light].hue = 28303
        lights[light].saturation = 217
        lights[light].brightness = 253

# set back original state
def set_original_state(lights, store_settings):
    for light in store_settings:
        
        lights[light].transitiontime = 1
        if store_settings[light]['on'] == True:
            lights[light].on = store_settings[light]['on']
            lights[light].hue = store_settings[light]['hue']
            lights[light].saturation = store_settings[light]['saturation']   
            lights[light].brightness = store_settings[light]['brightness']           
        else:
            lights[light].hue = store_settings[light]['hue']
            lights[light].saturation = store_settings[light]['saturation']
            lights[light].brightness = store_settings[light]['brightness'] 
            lights[light].on = store_settings[light]['on']
        
# blink lights
def blink_lights():
    
    # Define lights to blink
    alert_lights = ['Kitchen', 'Living Room', 'Living Room 2']

    # Hue bridge IP
    b = Bridge('192.168.2.4')

    # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
    b.connect()

    # Get the bridge state (This returns the full dictionary that you can explore)
    b.get_api()

    # Get all the Hue lights
    lights = b.get_light_objects('id')

    store_settings = {}

    for id in lights:
        if lights[id].name in alert_lights:
            state = {"on" : lights[id].on, 'hue': lights[id].hue, 'saturation': lights[id].saturation, 'brightness': lights[id].brightness}

            if store_settings.get(id) is None:
                store_settings[id] = state

    set_alert_state(lights, store_settings)

    # wait
    time.sleep(0.01)
    set_original_state(lights, store_settings)


# Run functions
def ding_dong():    
    print("Button is pressed")
    ring_bell()
    telegram_bot_sendtext("DING DONG!")
    blink_lights()

# Button press
button.when_pressed = ding_dong

pause()
