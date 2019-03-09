	###########################################
	# This autoBot is developed by Jitu Nayak #
	# Email id : jitunayak715@gmail.com       #
	###########################################

import pyautogui
import time
import numpy as np
import pyscreenshot as ImageGrab

def mimageGrab():
    x=240
    y=266
    box = (x,y,x+20,y+20)
    image = ImageGrab.grab(box)
    # grayImage = imageOps.grayImage(image)
    # a = array(grayImage.getcolors())
    a = np.asanyarray(image)
    b = a.sum()
    if(b<296400):
        pressSpace()
    #print(b)

def restartGame():
    pyautogui.click(325,444) 
    
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05) 
    print("Jump")
    pyautogui.keyUp('space')
    time.sleep(0.05)

while(True):
    x,y = pyautogui.position()
    #print(x,y,"\n")
    #time.sleep(2)
    mimageGrab()
