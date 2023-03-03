from modules.interface import Interface
from images.img import *
from time import sleep
from modules.moving import Moving

sleep(2)

# Инициализация бота
ui = Interface()
moving = Moving()

# Подготовка и поиск элементов интерфейса
ui.screenshot_gui()
overview, chat, spots, cargo, drones = 0, 0, 0, 0, 0
try:
    overview = ui.find_gui('overview')
    print('1. overview', overview)
    chat = ui.find_gui('chat')
    print('2. chat', chat)
    spots = ui.find_gui('spots')
    print('3. spots', spots)
    cargo = ui.find_gui('cargo')
    print('4. cargo', cargo)
    drones = ui.find_gui('drones')
    print('5. drones', drones)

except:
    pass
# resim = cv2.imread("./images/screenshot.png")
# for i in [overview, chat, spots, cargo, drones]:
#
#     cv2.imshow(f'{i}', resim[i[1]:i[3], i[0]:i[2]])
#     cv2.waitKey(0)
# cv2.destroyAllWindows()
moving.dock(spots)
