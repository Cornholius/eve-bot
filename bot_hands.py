import pyautogui
import pydirectinput
import numpy as np
from img import *
from time import sleep


class Logic:

    def dock(self):
        pydirectinput.rightClick()
        sleep(1)
        point = (pyautogui.position())
        print(point)
        menu = pyautogui.screenshot(region=(point[0], point[1], 180, 300))
        menu = cv2.cvtColor(np.array(menu), cv2.COLOR_RGB2BGR)
        cv2.imwrite('./images/1.png', menu)
        qwe = pyautogui.locate(dock, menu)
        print(qwe)
        pyautogui.moveTo(point[0] + qwe[0], point[1] + qwe[1])
        sleep(1)
        pydirectinput.leftClick()
