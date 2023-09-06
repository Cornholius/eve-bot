import random
from random import uniform
from pyautogui import locateOnScreen, locateCenterOnScreen
import pydirectinput
from images.img import citadel, gui, space
from time import sleep
from modules.IO import IO


# ui = Interface()
io = IO()


class Moving:

    @staticmethod
    def pause():
        sleep(random.uniform(0.3, 1.0))

    @staticmethod
    def round_menu():
        pos = pydirectinput.position()
        menu_area = (pos[0] - 100, pos[1] - 100, 200, 200)
        return menu_area

    @staticmethod
    def hotkey(key1=None, key2=None):
        pydirectinput.keyDown(key1)
        sleep(round(uniform(0.1, 0.7), 3))
        pydirectinput.keyDown(key2)
        sleep(round(uniform(0.1, 0.4), 3))
        pydirectinput.keyUp(key2)
        pydirectinput.keyUp(key1)

    def dock(self, coords):
        docking_spot = locateCenterOnScreen(citadel['dock_spot'], region=coords, confidence=.9)
        io.move(docking_spot)
        self.pause()
        pydirectinput.mouseDown()
        Moving.pause()
        dock_icon = locateCenterOnScreen(citadel['dock'], region=self.round_menu(), confidence=.9)
        io.move(dock_icon)
        Moving.pause()
        pydirectinput.mouseUp()

    def undock(self):
        while True:
            undock_button = locateCenterOnScreen(citadel['undock'])
            if undock_button:
                print('undock button found')
                break
            else:
                sleep(5)
        io.move(undock_button)
        self.pause()
        pydirectinput.leftClick()
        print('undocking...')
        while True:
            nav_panel_corner = locateOnScreen(gui['overview'][0])
            if nav_panel_corner:
                print('undock is done')
                break
            else:
                sleep(2)
        sleep(round(uniform(0.1, 1.5), 2))
        self.hotkey('ctrl', 'space')

    def go_to_spot(self, coords):
        spot_label = locateCenterOnScreen(space['spot'], region=coords, confidence=.9)
        io.move(spot_label)
        self.pause()
        pydirectinput.mouseDown()
        Moving.pause()
        warp_to_icon = locateCenterOnScreen(space['warp_to'], region=self.round_menu(), confidence=.9)
        io.move(warp_to_icon)
        Moving.pause()
        pydirectinput.mouseUp()

    @staticmethod
    def warping_done():
        sleep(2)
        while True:
            establishing_warp_vector = locateOnScreen(space['establishing_warp'])
            if establishing_warp_vector:
                print('establising warp')
                sleep(1)
            else:
                print('establising warp done')
                sleep(1)
                break

        while True:
            warp_is_active = locateOnScreen(space['warp_drive_active'])
            if warp_is_active:
                print('Warping')
                sleep(1)
            else:
                print('Warping in done')
                break
        return True
