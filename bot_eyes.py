import cv2
import numpy as np
from img import *


class Find:

    def find_mana(self, image):
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # преобразуем её в серую
        screenshot = cv2.imread('./images/test3.png', cv2.IMREAD_GRAYSCALE)  # скрин преобразуем в серый
        result = cv2.matchTemplate(gray_img, screenshot, cv2.TM_CCOEFF_NORMED)  # ищем на скрине объект
        loc = np.where(result >= 0.9)
        for pt in zip(*loc[::-1]):
            if pt is not None:
                return True