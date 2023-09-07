import random

import numpy as np
import pyautogui
from threading import Thread
from images.img import gui, screenshot
from modules.database import Database
from modules.IO import IO, Colors
from modules.interface import Interface
from modules.moving import Moving
from modules.drones import Drones
from modules.ratting import Ratting
from modules.mining import Mining
import cv2
from random import uniform
import time
import timeit
import pygetwindow as gw


import logging
import os
from time import sleep

logging.getLogger('ruautogui.mouse').setLevel(logging.INFO)
logging.getLogger('ruautogui.bezier').setLevel(logging.INFO)

# Проверяем наличие базы
if not os.path.exists('database.db'):
    print(f'{Colors.FAIL}База не найдена. Создаю новую')
    Database.initialization()

# настройки бота перед запуском (временно)
target_priority = ['frigate', 'battlecruiser']
miner_duration = 33
frendly_local = True

# Инициализация бота
db = Database()
io = IO()
ui = Interface()
moving = Moving()
drones = Drones()
ratting = Ratting(target_priority)
mining = Mining('EVE - Cornilita Rus', ['EVE - Corn812', "EVE - Salman Del'Pino"])


# Подготовка и поиск элементов интерфейса
ui.screenshot_gui()
resim = cv2.imread(screenshot)
for key in gui.keys():
    try:
        element_coords = ui.find_gui(key)
        db.add_coords(key, element_coords)
        print(Colors.OKGREEN, key, element_coords)
        # border = cv2.copyMakeBorder(resim, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,
        #                             borderType=cv2.BORDER_CONSTANT, value=[mean, mean, mean])

        # cv2.imshow(f'{key}', resim[element_coords[1]:element_coords[3], element_coords[0]:element_coords[2]])
        cv2.imwrite(f'./images/screenshots/{key}.png',
                    resim[element_coords[1]:element_coords[3], element_coords[0]:element_coords[2]])
        # cv2.waitKey(0)
    except Exception as error:
        print(Colors.FAIL, key, error)
# cv2.destroyAllWindows()

# тест команд
def check_for_hostile(*args):
    print('start looking for hostiles...')
    global frendly_local
    data = []
    for i in args:
        data.append(i)
    while True:
        sleep(1)
        # print(frendly_local)
        local = pyautogui.screenshot(region=(data[0], data[1], data[2] - data[0], data[3] - data[1]))
        local = cv2.cvtColor(np.array(local), cv2.COLOR_RGB2BGR)
        # cv2.imshow('123', local)
        # cv2.waitKey(0)
        red = [10, 10, 117]
        y, x = np.where(np.all(local == red, axis=2))
        if y.size > 0:
            frendly_local = False
        else:
            frendly_local = True


def mining_mode():
    total_time = 0
    print(f'{Colors.OKBLUE}start miming')
    while frendly_local:
        start = timeit.default_timer()
        if total_time > 20:
        # if total_time > random.uniform(miner_duration + 2.1, miner_duration + 20.5):
            sleep(uniform(1.6, 2.4))
            mining.check_cargo(mining.main_window)
            for window in mining.windows:
                window.maximize()
                # gw.getWindowsWithTitle(window)
                sleep(uniform(1.6, 2.4))
                mining.check_cargo(window)
                window.minimize()
            total_time = 0
        sleep(uniform(0.3, 1.3))
        total_time += timeit.default_timer() - start
        # gw.getWindowsWithTitle(mining.main_window)
        # print('still mining...')
    print(f'{Colors.FAIL}HOSTILE IN LOCAL!')


find_enemy = Thread(target=check_for_hostile, args=list(db.get_data('chat')))
bot_mode = Thread(target=mining_mode)
find_enemy.start()
bot_mode.start()

while True:
    sleep(10)
    if not bot_mode.is_alive():
        thread = Thread(target=mining_mode)
        thread.start()
# mining_mode()
# print('!!!!!!!!!!!!!!!!!!!!!!!')



# ratting.target_enemy()
# ratting.warp_to_anomalies('squad')
# moving.dock(db.get_data('spots'))
# while not moving.warping_done(): sleep(1)
# sleep(10)
# print('time to undock')
# moving.undock()
# moving.go_to_spot(db.get_data('spots'))
# while not moving.warping_done(): sleep(1)
# drones.launch_drones('heavy', db.get_data('drones'))
# sleep(5)
# drones.return_drones()
# print('all jobs done')
