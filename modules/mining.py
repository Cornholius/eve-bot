import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
from modules.database import Database
from pyautogui import locateOnScreen, locateCenterOnScreen, locateAllOnScreen
from images.img import mining
from modules.moving import Moving
from modules.IO import IO, Colors
import pydirectinput
from time import sleep
db = Database()


class Mining:

    def __init__(self, main_window, windows):
        self.main_window = gw.getWindowsWithTitle(main_window)[0]
        self.windows = [gw.getWindowsWithTitle(i)[0] for i in windows]
        self.cargo = db.get_data('cargo')
        self.count = 100

    # def get_window(self, window):
    #     window.maximize()
        # sleep(1)

    def check_cargo(self, window):
        if self.cargo_capacity(window.title[6:]) == 'full':
            if window.title == self.main_window.title:
                cargo = 'mining_hold'
            else:
                cargo = 'bonus_cargo'
            self.drop_to_bonus_ship(cargo)
        print(Colors.OKBLUE, window.title[6:], 'cargo is empty')

    def cargo_capacity(self, title):
        capacity_area = (252 + self.cargo[0], 33 + self.cargo[1], 120, 24)
        capacity = pyautogui.screenshot(region=capacity_area)
        capacity = cv2.cvtColor(np.array(capacity), cv2.COLOR_RGB2BGR)
        # cv2.imwrite(str(self.count) + '.png', capacity)
        self.count += 1
        # print(capacity[0, 90])
        if 48 < capacity[0, 90][0] < 53:
            print(Colors.WARNING, title, 'cargo is full!')
            return 'full'

    def drop_to_bonus_ship(self, cargo_type):
        stack_all_btn = locateCenterOnScreen(mining['stack_all'], region=self.cargo)
        ore_icon_coords = (206 + self.cargo[0], 104 + self.cargo[1])
        IO.move(stack_all_btn)
        Moving.pause()
        pydirectinput.leftClick()
        Moving.pause()
        Moving.hotkey('ctrl', 'a')
        Moving.pause()
        IO.move(ore_icon_coords)
        Moving.pause()
        pydirectinput.mouseDown()
        Moving.pause()
        big_cargo = locateCenterOnScreen(mining[cargo_type])
        IO.move(big_cargo)
        Moving.pause()
        pydirectinput.mouseUp()
