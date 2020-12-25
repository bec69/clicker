import pyautogui
import time

time.sleep(2)
pyautogui.keyDown('shift')
pyautogui.mouseDown(button='right')
time.sleep(128)
pyautogui.keyUp('shift')
pyautogui.mouseUp(button='right')
