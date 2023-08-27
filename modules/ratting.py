from pyautogui import locateOnScreen, locateCenterOnScreen
from images.img import light_drones, medium_drones, heavy_drones, sentry_drones


class Drones():

    def launch_drones(self):
        drone_group = locateCenterOnScreen(, region=coords, confidence=.9)