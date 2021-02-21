# Raspberry Pi Doorbell
The purpose of this script is to create a smart doorbell from an existing wireless dooorbell.  
What it does:
- Ring the doorbell
- Send a telegram message
- Blink Philips Hue lights

https://djurre-draaisma.medium.com/ive-transformed-a-cheap-wireless-doorbell-to-a-smart-doorbell-10fa4e73fd00
  
# Requirements
- A wireless doorbell which runs at 3 volt batteries, but those batteries should be removed.
- Philips Hue  
- A phone with Telegram
- PHUE (https://github.com/studioimaginaire/phue)  
- Gpiozero (https://gpiozero.readthedocs.io/en/stable/)

# Setup

- Doorbell modifications:  
The doorbell transmitter needs some modification. The battery connectors should be wired to the GPIO connections and the switch should always be in a press-in state.
The Raspberry provides 3.3 Volts In my case this wasn't an issue, but it can be an issue for other doorbells.
Warning: You can damage it irreparably. I am not responsible for any damage. Everything you do is at your own risk. 

- Telegram:  
Create a Telegram Bot (https://core.telegram.org/bots) and start a conversation with the bot. You need to get the chat id from you and your bot.
The chat ID can be found when doing an API call to https://api.telegram.org/bot' + bot_token + '/getUpdates  
Once created, just replace the bot_token and bot_chatID variables.  
  
- Hue:  
Replace the Hue bridge IP with the IP of your Hue bridge.
Add the names of the lights which you want to blink to alert_lights.  
You can change the hue, saturation and brightness settings to whatever you want.
  
Connect the button to the GPIO2 and a ground connection. Connect the battery connections to (+)GPIO22 (-)Ground. Other GPIO connector can be used.
The gpiozero docs provide a clear overview of the pins.
https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
