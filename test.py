import ctypes
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
from PIL import Image

# Инициализация бота
eyes = Find()
hands = Logic()
screenshot = cv2.imread('images/screenshot.png')

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
def find_ui(image):
    corner1 = pyautogui.locate(gui[image][0], screenshot, confidence=.75)  # ищем левый верхний угол
    print(image, 'corner 1', corner1)
    resim = cv2.imread("./images/screenshot.png")
    if corner1[0] < 700:
        area = resim[corner1[1]:height, corner1[0]:width//3]
    else:
        area = resim[corner1[1]:height, corner1[0]:width]
    corner2 = pyautogui.locate(gui[image][1], area, confidence=.90)  # ищем левый верхний угол

    print(image, 'corner 2', corner2)
    final = area[0:corner2[1]+corner2[3], 0:corner2[0]+corner2[2]]
    # [y начало: y на сколько вниз, x начало: x на сколько влево]
    cv2.imshow(image, final)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('./images/{}.png'.format(image), final)
    print(corner1[0], corner1[1], corner2[0]+corner2[2]+corner1[0], corner2[1]+corner2[3]+corner1[1])
    gui_borders_coord = (corner1[0], corner1[1], corner2[0]+corner2[2]+corner1[0], corner2[1]+corner2[3]+corner1[1])

find_ui('overview')
find_ui('chat')
find_ui('cargo')
find_ui('spots')
find_ui('drones')

# temp_screen = pyautogui.screenshot(region=(corner1[0], corner1[1], 1920-corner1[0], 1024-corner1[1]))
# www = cv2.cvtColor(np.array(temp_screen), cv2.COLOR_RGB2BGR)
# cv2.imwrite('./images/temp.png', temp_screen)
# qwe = cv2.imread('./images/temp.png')
# cv2.imshow('123', qwe)