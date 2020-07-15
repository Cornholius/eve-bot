import pyautogui
import pydirectinput
import numpy as np
from img import *
from time import sleep


class Logic:

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

    def go_to_spot(self, coords):
        q = pyautogui.locateCenterOnScreen(spot, region=coords, confidence=.75)
        pyautogui.dragTo(q)
        sleep(0.3)
        pydirectinput.rightClick()
        sleep(0.3)
        pyautogui.moveTo(q[0] + 40, q[1] + 10)
        sleep(0.3)
        pydirectinput.leftClick()
