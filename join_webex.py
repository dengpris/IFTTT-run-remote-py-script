"""
Created on July 15 2022

@author: Priscilla
"""

import pyautogui
import webbrowser  
import time

############# HELPER FUNCTIONS ##############

def FindAndClick(image, starttime, timeout):
    x, y = None, None
    while((x, y == None, None) and (time.time() < (starttime + timeout))):
        x, y = pyautogui.locateCenterOnScreen(image, confidence=0.8)
    pyautogui.click(x, y)    


################ HELPERS END ################

alvaro_webex_url = 'https://bellcollab.webex.com/meet/alvaro.morataya'
timeout = 5

webbrowser.open(alvaro_webex_url, new=1)
time.sleep(1)
join_start = time.time()

# Click "Join as Guest"
FindAndClick('join_as_guest.png', join_start, timeout)
time.sleep(1)

# Click "Join Meeting"
join_start = time.time()
FindAndClick('join_meeting.png', join_start, timeout)
