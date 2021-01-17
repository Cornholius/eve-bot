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

sleep(1)

# Инициализация бота
eyes = Find()
hands = Logic()
# Подготовка и поиск элементов интерфейса
eyes.screenshot_gui()
try:
    overview = eyes.find_gui(gui['overview'], '!overview')
    print('overview ready')
    chat = eyes.find_gui(gui['chat'], '!chat')
    print('chat ready')
    spots = eyes.find_gui(gui['spots'], '!spots')
    print('spots ready')
    cargo = eyes.find_gui(gui['cargo'], '!cargo')
    print('cargo ready')
    # drones = eyes.find_gui(gui['drones'], '!drones')
    # print('drones ready')

except:
    pass
# hands.go_to_spot(spots)
# sleep(3)

# while True:
#     sleep(1)
#     qwe = pyautogui.locateOnScreen(warp, confidence=.75)
#     if qwe is None:
#         break
#     print(qwe)
# hands.dock(overview)
# qwe = eyes.find_object_in_overview(fortizar, overview)
# www = pyautogui.screenshot(region=chat)
# www =cv2.cvtColor(np.array(www), cv2.COLOR_RGB2BGR)
# cv2.imwrite('./images/12.png', www)