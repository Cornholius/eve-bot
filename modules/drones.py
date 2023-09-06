from pyautogui import locateOnScreen, locateCenterOnScreen
from time import sleep
from images.img import drone
from modules.moving import Moving
from modules.IO import IO
import pydirectinput


class Drones:

    def launch_drones(self, group, coords):
        current_group = locateCenterOnScreen(drone[group], region=coords, confidence=.9)
        IO.move(current_group)
        Moving.pause()
        pydirectinput.mouseDown()
        Moving.pause()
        launch_icon = locateCenterOnScreen(drone['launch'], region=Moving.round_menu(), confidence=.9)
        IO.move(launch_icon)
        Moving.pause()
        pydirectinput.mouseUp()

    def return_drones(self):
        Moving.hotkey('shift', 'r')

    def engage(self):
        Moving.hotkey('shift', 'r')
