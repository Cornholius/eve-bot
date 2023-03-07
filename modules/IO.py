from pyautogui import moveTo
from time import sleep
from ruautogui import mouse

class IO:

    def move(self, end_point):
        inaccuracy = 7
        box = [
            end_point[0] - inaccuracy,
            end_point[0] + inaccuracy,
            end_point[1] - inaccuracy,
            end_point[1] + inaccuracy
        ]

        while True:
            mouse.move(end_point)
            mouse_position = mouse.get_mouse_cursor_position()
            if box[0] < mouse_position[0] < box[1] and box[2] < mouse_position[1] < box[3]:
                break
