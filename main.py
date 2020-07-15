from time import sleep
import pyautogui
import pydirectinput
import cv2
import numpy as np
from bot_eyes import Find
from img import *
from time import sleep
import time
from bot_hands import Logic


sleep(2)
eyes = Find()
hands = Logic()
eyes.screenshot_gui()
eyes.find_gui(overview_border_start)
coord = eyes.find_object(fortizar)
hands.dock()
