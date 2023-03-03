from random import uniform
import pyautogui
import pydirectinput
from images.img import *
from time import sleep
import numpy as np
import ctypes

class Moving:

    def dock(self, coords):
        q = pyautogui.locateCenterOnScreen(dock_spot, region=coords, confidence=.9)
        pyautogui.dragTo(q)
        sleep(0.3)
        pydirectinput.rightClick()
        sleep(0.3)
        w = pyautogui.locateCenterOnScreen(dock, region=coords, confidence=.9)
        pyautogui.moveTo(w)
        sleep(0.3)
        pydirectinput.leftClick()

    def undock(self):
        width = ctypes.windll.user32.GetSystemMetrics(0)
        height = ctypes.windll.user32.GetSystemMetrics(1)
        undock_screen_area = pyautogui.screenshot(region=(width * 0.75, 0, width * 0.25, height * 0.4))
        undock_button = pyautogui.locate(undock, undock_screen_area)
        pyautogui.moveTo(undock_button.left + width * 0.75, undock_button.top)
        sleep(0.3)
        pydirectinput.leftClick()



        # while True:
        #     undock_button = pyautogui.locateCenterOnScreen(undock, region=(1500, 100, 1900, 400), confidence=.75)
        #     if undock_button is not None:
        #         sleep(3)
        #         break
        # pyautogui.dragTo(undock_button)
        # sleep(round(uniform(0.3, 1.1), 2))
        # pydirectinput.leftClick()
        # while True:
        #     qwe = pyautogui.locateOnScreen(gui['overview'][0], region=coords, confidence=.75)
        #     if qwe is not None:
        #         sleep(1)
        #         break
        # sleep(round(uniform(3.1, 7.5), 2))
        # self.hotkey('ctrl', 'space')

    def go_to_spot(self, coords):
        print('coords', coords)
        q = pyautogui.locateCenterOnScreen(spot, region=coords, confidence=.9)
        print('go_to_spot', q)
        pyautogui.moveTo(q)
        sleep(1)
        pydirectinput.rightClick()
        sleep(1)
        q2 = pyautogui.locateCenterOnScreen(warp_to, region=coords, confidence=.9)
        pyautogui.moveTo(q2)
        sleep(1)
        pydirectinput.leftClick()