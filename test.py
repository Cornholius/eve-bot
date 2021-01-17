from time import sleep
import pyautogui
import pydirectinput
import cv2
import numpy as np
from bot_eyes import Find
from img import *
from time import sleep
import time
from bot_hands import Logic

# Инициализация бота
eyes = Find()
hands = Logic()
screenshot = cv2.imread('images/screenshot.png')
corner1 = pyautogui.locate(gui['overview'][0], screenshot, confidence=.75)  # ищем левый верхний угол
corner2 = pyautogui.locate(gui['overview'][1], screenshot, confidence=.75)  # ищем левый верхний угол
print(corner1)
print(corner2)
temp_screen = pyautogui.screenshot(region=(corner1[0], corner1[1], 1920-corner1[0], 1024-corner1[1]))
www = cv2.cvtColor(np.array(temp_screen), cv2.COLOR_RGB2BGR)
cv2.imwrite('./images/temp.png', temp_screen)
qwe = cv2.imread('./images/temp.png')
cv2.imshow('123', qwe)