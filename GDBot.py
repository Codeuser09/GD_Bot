import pyautogui
import time
import keyboard
import mouse
import win32api, win32con

ClickDelay = 1 #How long it takes to move/press/release the cursor in the Click function
BtwClickDelay = 3 #How long it takes between every Click
ScanFrequency = 20 #How long it takes before the next scan
StartDelay = 5 #How much time you have before the programm starts
ScrollTime = 1 #How much time it takes for you to scroll to the next level

AmountOfBeatenLevels = 0 #The amount of levels you have beaten
AmountOfLevels = 7 #The amount of levels/Page you wanna beat

#pyautogui.displayMousePosition()

'''
Basically the programm scans if you have completet a level every <ScanFrequency> Seconds and presses the inputs needed
to go into a new level and repeat.
Start this programm while you are already in your first auto level
'''
#924 Y:  195
#926 Y:  901
    
'''
    Click DOCS:

    #Just escape
    keyboard.press_and_release("Escape")
    
    #Play level
    Click(955, 382)
    time.sleep(3)
    
    #Skip no song
    Click(1111, 763)
    time.sleep(3)
    
    #Viewing level
    Click(1399, 347)
    
    #Next page
    Click(1822, 530)
    time.sleep(3)
    
    #Unpause
    Click(954, 720)
    
    
    pyautogui.keyDown('a')
time.sleep(CurrentScrollTime)
pyautogui.keyUp('a')
print("Scrolled")
'''

time.sleep(StartDelay)

def Scroll(x1, y1, x2, y2): #Scrolling from x1 and y1 to x2 and y2
    pyautogui.moveTo(x1, y1)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(x2, y2, ScrollTime)
    pyautogui.mouseUp(button='left')

def Click(x, y): #Just Clicking
    win32api.SetCursorPos((x, y))
    time.sleep(ClickDelay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(ClickDelay)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def AltTab(): #AltTabbing
    pyautogui.keyDown("Alt")
    pyautogui.keyDown("Tab")
    pyautogui.keyUp("Alt")
    pyautogui.keyUp("Tab")
      
while not keyboard.is_pressed('S'): #Main Loop(Stopped with S)

    #AltTabbing twice and unpausing the game(To update image recognition)
    AltTab()
    AltTab()
    Click(954, 720)
    
    #Trying to locate level end screen
    if pyautogui.locateOnScreen('GDPic.png') != None:
        print("Level finished")
        
        AmountOfBeatenLevels = AmountOfBeatenLevels + 1
        
        #Pressing Escape twice
        keyboard.press_and_release("Escape")
        print("Escaped")
        time.sleep(BtwClickDelay)
        keyboard.press_and_release("Escape")
        print("Escaped")
        time.sleep(BtwClickDelay)
        
        #Resetting the scroll position
        Scroll(924, 195, 924, 901)
        Scroll(924, 195, 924, 901)
        Scroll(924, 195, 924, 901)
        time.sleep(BtwClickDelay)
        
        #Scrolling to the next lvl
        for x in range(AmountOfBeatenLevels):
            Scroll(1399, 347, 1399, 37)
        
        #Going to the next page of auto levels if the levels on the page are played
        if AmountOfBeatenLevels == AmountOfLevels:
            Click(1822, 530)
            print("Clicked")
            AmountOfBeatenLevels = 0
            time.sleep(BtwClickDelay)
        
        #Viewing the level
        Click(1399, 347)
        print("Clicked")
        time.sleep(BtwClickDelay + 5)
        
        #Playing the level
        Click(955, 382)
        print("Clicked")
        time.sleep(BtwClickDelay)
        
    else:   
        print("Still in the level")
        
    #Waiting for the scan frequency before the next loop starts
    time.sleep(ScanFrequency)