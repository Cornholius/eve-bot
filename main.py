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
ui = {'overview': '', 'chat': '', 'spots': '', 'cargo': '', 'drones': ''}
for i in ui:
    try:
        element = eyes.find_gui(gui[i])
        ui[i] = element
        region = (element[0], element[1], element[2] - element[0], element[3] - element[1])
        www = pyautogui.screenshot(region=region)
        www = cv2.cvtColor(np.array(www), cv2.COLOR_RGB2BGR)
        cv2.imwrite('./images/!{}.png'.format(i), www)
        print(i, element)
    except:
        pass
# hands.dock(ui['spots'])
# while True:
#     qwe = pyautogui.locateOnScreen(gui['overview'][0], region=ui['overview'], confidence=.75)
#     if qwe is None:
#         sleep(3)
#         break
hands.undock(ui['overview'])
# hands.undock(ui['overview'])
# sleep(3)
#
# while True:
#     sleep(1)
#     qwe = pyautogui.locateOnScreen(warp, confidence=.75)
#     if qwe is None:
#         break
# sleep(3)
# pydirectinput.press('F1')

# hands.dock(ui['overview'])
# qwe = eyes.find_object_in_overview(fortizar, overview)
# www = pyautogui.screenshot(region=chat)
# www =cv2.cvtColor(np.array(www), cv2.COLOR_RGB2BGR)
# cv2.imwrite('./images/12.png', www)