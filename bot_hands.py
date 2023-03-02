from random import uniform
import pyautogui
import pydirectinput
import numpy as np
from img import *
from time import sleep


class Logic:

    def hotkey(self, key1=None, key2=None):
        pydirectinput.keyDown(key1)
        pydirectinput.keyDown(key2)
        sleep(round(uniform(0.1, 0.7), 3))
        pydirectinput.keyUp(key2)
        pydirectinput.keyUp(key1)

    def dock(self, coords):
        q = pyautogui.locateCenterOnScreen(fortizar, region=coords, confidence=.75)
        pyautogui.dragTo(q)
        sleep(0.3)
        pydirectinput.rightClick()
        sleep(0.3)
        w = pyautogui.locateCenterOnScreen(dock, region=coords, confidence=.75)
        pyautogui.moveTo(w)
        sleep(0.3)
        pydirectinput.leftClick()

    def undock(self, coords):
        while True:
            undock_button = pyautogui.locateCenterOnScreen(undock, region=(1500, 100, 1900, 400), confidence=.75)
            if undock_button is not None:
                sleep(3)
                break
        pyautogui.dragTo(undock_button)
        sleep(round(uniform(0.3, 1.1), 2))
        pydirectinput.leftClick()
        while True:
            qwe = pyautogui.locateOnScreen(gui['overview'][0], region=coords, confidence=.75)
            if qwe is not None:
                sleep(1)
                break
        sleep(round(uniform(3.1, 7.5), 2))
        self.hotkey('ctrl', 'space')

    def go_to_spot(self, coords):
        print('coords', coords)
        q = pyautogui.locateCenterOnScreen(spot, region=coords, confidence=.65)
        print('go_to_spot', q)
        pyautogui.dragTo(q)
        sleep(0.3)
        pydirectinput.rightClick()
        sleep(0.3)
        pyautogui.moveTo(q[0] + 40, q[1] + 10)
        sleep(0.3)
        pydirectinput.leftClick()
