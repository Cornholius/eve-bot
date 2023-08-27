# resim = cv2.imread("./images/screenshot.png")
# for i in [overview, chat, spots, cargo, drones]:
#
#     cv2.imshow(f'{i}', resim[i[1]:i[3], i[0]:i[2]])
#     cv2.waitKey(0)
# cv2.destroyAllWindows()

import pyautogui
import cv2
import numpy as np
import pydirectinput

pos = pydirectinput.position()
menu_area = (pos[0], pos[1], 200, 200)
full_screenshot = pyautogui.screenshot(region=menu_area)
full_screenshot = cv2.cvtColor(np.array(full_screenshot), cv2.COLOR_RGB2BGR)
cv2.imwrite('./images/round_menu.png', full_screenshot)
resim = cv2.imread("./images/round_menu.png")
cv2.imshow(resim)
cv2.waitKey(0)