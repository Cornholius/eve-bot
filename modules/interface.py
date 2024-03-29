import numpy as np
import pyautogui

from images.img import *
from pyautogui import dragTo, locate
import ctypes
from images.img import screenshot


class Interface:

    def __init__(self):
        user32 = ctypes.windll.user32
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)

    def screenshot_gui(self):
        full_screenshot = pyautogui.screenshot()
        full_screenshot = cv2.cvtColor(np.array(full_screenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite(screenshot, full_screenshot)

    def find_gui(self, image, screen=None):
        screen = cv2.imread(screenshot)
        corner1 = locate(gui[image][0], screen, confidence=.90)  # ищем левый верхний угол
        if corner1[0] < 700:  # если элемент слева, то ищем в 1/3 ширине экрана
            area = screen[(corner1[1] + 100):self.height, corner1[0]:self.width // 3]
        else:
            area = screen[(corner1[1] + 100):self.height, corner1[0]:self.width]
        corner2 = locate(gui[image][1], area, confidence=.90)  # отсекаем лишние и ищем правый нижний угол
        gui_borders_coord = (corner1[0],
                             corner1[1],
                             corner2[0] + corner2[2] + corner1[0],
                             corner2[1] + corner2[3] + corner1[1] + 100)
        return gui_borders_coord

    def find_object_in_overview(self, image, coords):
        object_screenshot = screenshot(region=coords)
        ingame_object = locate(image, object_screenshot)
        coordinates = [coords[0] + ingame_object[0] + (ingame_object[2] / 2),
                       coords[1] + ingame_object[1] + (ingame_object[3] / 2)]
        dragTo(coordinates[0], coordinates[1])
