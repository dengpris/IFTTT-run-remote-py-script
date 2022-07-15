from flask import Flask
from flask import request

import pyautogui
import webbrowser  
import time
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello!'

def FindAndClick(image, starttime, timeout):
    x, y = None, None
    while((x, y == None, None) and (time.time() < (starttime + timeout))):
        x, y = pyautogui.locateCenterOnScreen(image, confidence=0.8)
    pyautogui.click(x, y)    


@app.route('/ifttt')
def handler(): 
    meeting_url = os.getenv('MEETING_URL')
    timeout = 5

    webbrowser.open(meeting_url, new=1)
    time.sleep(2)
    join_start = time.time()

    # Click "Join as Guest"
    FindAndClick('join_as_guest.png', join_start, timeout)
    time.sleep(1)

    # Click "Join Meeting"
    join_start = time.time()
    FindAndClick('join_meeting.png', join_start, timeout)
