from images.img import gui
from modules.database import Database
from modules.IO import IO
from modules.interface import Interface
from modules.moving import Moving
from modules.drones import Drones

import logging
import os
from time import sleep


logging.getLogger('ruautogui.mouse').setLevel(logging.INFO)
logging.getLogger('ruautogui.bezier').setLevel(logging.INFO)

# Проверяем наличие базы
if not os.path.exists('database.db'):
    print('База не найдена. Создаю новую')
    Database.initialization()

# Инициализация бота
db = Database()
io = IO()
ui = Interface()
moving = Moving()
drones = Drones()


# Подготовка и поиск элементов интерфейса
ui.screenshot_gui()
for key in gui.keys():
    try:
        element_coords = ui.find_gui(key)
        db.add_coords(key, element_coords)
        print(key, 'найден и добавлен')
    except Exception as error:
        print(error, key, 'не найден!')

# тест команд
drones.launch_drones('heavy', db.get_data('drones'))
sleep(5)
drones.launch_drones('sentry', db.get_data('drones'))
sleep(5)
drones.launch_drones('light', db.get_data('drones'))
sleep(5)
drones.launch_drones('mediun', db.get_data('drones'))
# moving.dock(db.get_data('spots'))
# while not moving.warping_done(): sleep(1)
# moving.undock()
# moving.go_to_spot(db.get_data('spots'))
# while not moving.warping_done(): sleep(1)
print('all jobs done')
