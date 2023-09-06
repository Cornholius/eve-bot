from modules.moving import Moving
from modules.IO import IO
from modules.database import Database
from pyautogui import locateOnScreen, locateCenterOnScreen, locateAllOnScreen
import pydirectinput
from images.img import drone, ratting, space, gui
from time import sleep


class Ratting:

    def __init__(self, target_priority):
        self.db = Database()
        self.target_priority = target_priority

    def toggle_prob_scaner_window(self):
        Moving.hotkey('alt', 'p')
        Moving.pause()

    def warp_to_anomalies(self, name):
        coords = self.db.get_data('probe_scanner')
        anomaly = locateCenterOnScreen(ratting[name], region=coords, confidence=.9)
        IO.move(anomaly)
        Moving.pause()
        pydirectinput.rightClick()
        Moving.pause()
        warp_icon = locateCenterOnScreen(space['warp_to_pkm'], region=coords, confidence=.9)
        IO.move(warp_icon)
        Moving.pause()
        pydirectinput.leftClick()
        while not Moving.warping_done(): sleep(1)
        Moving.pause()
        print('Приехал на аномальку')

    def target_enemy(self):
        region = self.db.get_data('overview')
        count = 0
        targets = []
        print(self.target_priority)
        for i in self.target_priority:
            for pos in locateAllOnScreen(ratting[i], region=region, confidence=.9):
                IO.move(pos)
                Moving.pause()
                pydirectinput.keyDown('ctrl')
                Moving.pause()
                pydirectinput.leftClick()
                pydirectinput.keyUp('ctrl')
                Moving.pause()
        print(targets)
        # IO.move(target)
        # Moving.pause()
        # pydirectinput.keyDown('ctrl')
        # Moving.pause()
        # pydirectinput.leftClick()


