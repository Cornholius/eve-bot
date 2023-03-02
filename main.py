import pyautogui
from bot_eyes import Find
from img import *
from time import sleep
from bot_hands import Logic

sleep(2)

# Инициализация бота
eyes = Find()
hands = Logic()

# Подготовка и поиск элементов интерфейса
eyes.screenshot_gui()
overview, chat, spots, cargo, drones = 0, 0, 0, 0, 0

try:
    overview = eyes.find_gui(gui['overview'])
    print('1. overview', overview)
    chat = eyes.find_gui(gui['chat'])
    print('2. chat', chat)
    spots = eyes.find_gui(gui['spots'])
    print('3. spots', spots)
    cargo = eyes.find_gui(gui['cargo'])
    print('4. cargo', cargo)
    drones = eyes.find_gui(gui['drones'])
    print('5. drones', drones)

except:
    pass
# hands.undock()
# sleep(5)
# hands.go_to_spot(spots)
# sleep(3)
#
# while True:
#     sleep(1)
#     qwe = pyautogui.locateOnScreen(warp, confidence=.75)
#     if qwe is None:
#         break
#     print(qwe)
# hands.dock(overview)
# qwe = eyes.find_object_in_overview(fortizar, overview)
# www = pyautogui.screenshot(region=chat)
# www =cv2.cvtColor(np.array(www), cv2.COLOR_RGB2BGR)
# cv2.imwrite('./images/12.png', www)


def test():
    hands.dock(overview)
    sleep(7)
    hands.undock(overview)
    sleep(5)
    hands.go_to_spot(spots)
    sleep(3)
    while True:
        sleep(1)
        qwe = pyautogui.locateOnScreen(warp, confidence=.75)
        if qwe is None:
            break
    sleep(2)
    hands.dock(overview)


if __name__ == "main":
    test()
