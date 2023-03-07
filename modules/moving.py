import random
from random import uniform
import pyautogui
import pydirectinput
from images.img import *
from time import sleep
import numpy as np
import ctypes
from ruautogui import mouse as ms
from ruautogui import keyboard as kb
from modules.interface import Interface
from modules.IO import IO

# ui = Interface()
io = IO()
class Moving:

    def hotkey(self, key1=None, key2=None):
        pydirectinput.keyDown(key1)
        sleep(round(uniform(0.1, 0.7), 3))
        pydirectinput.keyDown(key2)
        sleep(round(uniform(0.1, 0.4), 3))
        pydirectinput.keyUp(key2)
        pydirectinput.keyUp(key1)
    def pause(self):
        sleep(random.uniform(0.3, 1.0))

    def dock(self, coords):
        q = pyautogui.locateCenterOnScreen(dock_spot, region=coords, confidence=.9)
        # ms.move(q)
        io.move(q)
        self.pause()
        pydirectinput.rightClick()
        self.pause()
        w = pyautogui.locateCenterOnScreen(dock, region=coords, confidence=.9)
        print('dock coords', w)
        # ms.move(w)
        io.move(w)
        self.pause()
        pydirectinput.leftClick()

    def undock(self):
        width = ctypes.windll.user32.GetSystemMetrics(0)
        height = ctypes.windll.user32.GetSystemMetrics(1)
        undock_screen_area = pyautogui.screenshot(region=(width * 0.75, 0, width * 0.25, height * 0.4))
        undock_button = pyautogui.locateCenterOnScreen(undock)
        print('dock coords', undock_button)
        # ms.move((int(undock_button.left + width * 0.75), int(undock_button.top)))
        # print((int(undock_button.left + width * 0.75), int(undock_button.top)))
        # io.move(end_point=[int(undock_button.left + width * 0.75), int(undock_button.top)])
        io.move(undock_button)
        self.pause()
        pydirectinput.leftClick()
        while True:
            qwe = pyautogui.locateOnScreen('images/gui/overview_border_start.png')
            if qwe is not None:
                # sleep(1)
                break
        sleep(round(uniform(0.1, 1.5), 2))
        self.hotkey('ctrl', 'space')

    def go_to_spot(self, coords):
        q = pyautogui.locateCenterOnScreen(spot, region=coords, confidence=.9)
        print('spot coords', q)

        # ms.move(q)
        io.move(q)
        self.pause()
        pydirectinput.rightClick()
        self.pause()
        q2 = pyautogui.locateCenterOnScreen(warp_to, region=coords, confidence=.9)
        # ms.move(q2)
        io.move(q2)
        self.pause()
        pydirectinput.leftClick()
        sleep(15)

        while True:
            qwe = pyautogui.locateOnScreen('images/space/warping.png')
            if qwe is None:
                break
            sleep(1)
