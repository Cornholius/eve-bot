import numpy as np
from img import *
import pyautogui
import ctypes


class Find:

    def __init__(self):
        user32 = ctypes.windll.user32
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)
        self.object_screenshot = ''
        self.gui_coordinates = ''

    def screenshot_gui(self):
        full_screenshot = pyautogui.screenshot()
        full_screenshot = cv2.cvtColor(np.array(full_screenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite('./images/screenshot.png', full_screenshot)

    def find_gui(self, image):
        left_top_corner = pyautogui.locate(image, screenshot)
        right_border = self.width - left_top_corner[0]
        bottom_border = self.height - left_top_corner[1]
        temporary_screenshot = pyautogui.screenshot(region=(left_top_corner[0],
                                                            left_top_corner[1],
                                                            right_border,
                                                            bottom_border))
        right_bottom_corner_startpoint = pyautogui.locate(overview_border_end, temporary_screenshot)
        h_end = right_bottom_corner_startpoint[1] + right_bottom_corner_startpoint[3]
        w_end = right_bottom_corner_startpoint[0] + right_bottom_corner_startpoint[2]
        object_screenshot = pyautogui.screenshot(region=(left_top_corner[0], left_top_corner[1], w_end, h_end))
        object_screenshot = cv2.cvtColor(np.array(object_screenshot), cv2.COLOR_RGB2BGR)
        self.object_screenshot = object_screenshot
        self.gui_coordinates = pyautogui.locateOnScreen(object_screenshot)
        cv2.imwrite('./images/1.png', object_screenshot)

    def find_object(self, image):
        w, h = self.gui_coordinates[0], self.gui_coordinates[1]
        ingame_object = pyautogui.locate(image, self.object_screenshot)
        coordinates = [w + ingame_object[0] + (ingame_object[2] / 2),
                       h + ingame_object[1] + (ingame_object[3] / 2)]
        pyautogui.dragTo(coordinates[0], coordinates[1])
