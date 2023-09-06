from ruautogui import mouse


class IO:

    @staticmethod
    def move(end_point):
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


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
