import numpy as np
from img import *
import pyautogui
import ctypes


class Find:

    def __init__(self):
        user32 = ctypes.windll.user32
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)

    def screenshot_gui(self):
        full_screenshot = pyautogui.screenshot()
        full_screenshot = cv2.cvtColor(np.array(full_screenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite('./images/screenshot.png', full_screenshot)

    def find_gui(self, image, name):
        left_top_corner = pyautogui.locate(image[0], screenshot, confidence=.75)  # ищем левый верхний угол
        right_border = self.width - left_top_corner[0]
        bottom_border = self.height - left_top_corner[1]
        temporary_screenshot = pyautogui.screenshot(
            region=(left_top_corner[0], left_top_corner[1], right_border, bottom_border))  # отрезаем лишнее

        www = pyautogui.screenshot(region=(left_top_corner[0], left_top_corner[1], right_border, bottom_border))
        www = cv2.cvtColor(np.array(www), cv2.COLOR_RGB2BGR)
        cv2.imwrite('./images/temp.png', www)

        right_bottom_corner = pyautogui.locate(image[1], temporary_screenshot)  # ищем правый нижний угол
        pyautogui.moveTo(right_bottom_corner[0] + left_top_corner[0], right_bottom_corner[1] + left_top_corner[1])
        x_start = left_top_corner[0]
        y_start = left_top_corner[1]
        x_end = right_bottom_corner[0] + right_bottom_corner[3]
        y_end = right_bottom_corner[1] + right_bottom_corner[2]
        gui_borders_coord = (x_start, y_start, x_end, y_end)

        www = pyautogui.screenshot(region=gui_borders_coord)
        www = cv2.cvtColor(np.array(www), cv2.COLOR_RGB2BGR)
        cv2.imwrite('./images/{}.png'.format(name), www)

        return gui_borders_coord

    def find_object_in_overview(self, image, coords):
        object_screenshot = pyautogui.screenshot(region=coords)
        ingame_object = pyautogui.locate(image, object_screenshot)
        coordinates = [coords[0] + ingame_object[0] + (ingame_object[2] / 2),
                       coords[1] + ingame_object[1] + (ingame_object[3] / 2)]
        pyautogui.dragTo(coordinates[0], coordinates[1])
