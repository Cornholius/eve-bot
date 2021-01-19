import pyautogui
import pydirectinput
from img import *
from time import sleep
from random import randint, uniform


class Logic:

    def hotkey(self, key1, key2):
        pydirectinput.keyDown(key1)
        pydirectinput.keyDown(key2)
        sleep(round(uniform(0.1, 0.7), 3))
        pydirectinput.keyUp(key2)
        pydirectinput.keyUp(key1)

    def dock(self, coords):
        dock_coord = pyautogui.locateCenterOnScreen(dock_spot, region=coords, confidence=.75)
        pyautogui.dragTo(dock_coord)
        sleep(round(uniform(0.3, 1.1), 2))
        pydirectinput.rightClick()
        sleep(round(uniform(0.3, 1.1), 2))
        pyautogui.moveTo(dock_coord[0] + randint(30, 120), dock_coord[1] - randint(4, 15))
        sleep(round(uniform(0.3, 1.1), 2))
        pydirectinput.leftClick()

    def undock(self, coords):
        undock_button = pyautogui.locateCenterOnScreen(undock, region=(1500, 100, 1900, 400), confidence=.75)
        pyautogui.dragTo(undock_button)
        sleep(round(uniform(0.3, 1.1), 2))
        pydirectinput.leftClick()
        while True:
            qwe = pyautogui.locateOnScreen(gui['overview'][0], region=coords, confidence=.75)
            if qwe is not None:
                break
        sleep(round(uniform(3.1, 7.5), 2))
        self.hotkey('ctrl', 'space')
