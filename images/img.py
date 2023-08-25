import cv2

# общее
screenshot = cv2.imread('./images/screenshot.png')

# стенды
plus = cv2.imread('images/standings/plus.png')
minus1 = cv2.imread('images/standings/minus1.png')
minus2 = cv2.imread('images/standings/minus2.png')

# цитадели
dock = cv2.imread('images/citadel/dock.png')
undock = cv2.imread('images/citadel/undock.png')
spot = cv2.imread('images/citadel/spot.png')
dock_spot = cv2.imread('images/citadel/dock_spot.png')

# в космосе
establishing_warp = cv2.imread('images/space/establishing.png')
warp_drive_active = cv2.imread('images/space/warp_drive_active.png')
warp = cv2.imread('images/space/warp.png')
warp_to = cv2.imread('images/space/warp_to.png')

every_border_end = cv2.imread('images/gui/every_border_end.png')
gui = {'overview': (cv2.imread('images/gui/overview_border_start.png'), every_border_end),
       'chat': (cv2.imread('images/gui/chat_border_start.png'), every_border_end),
       'cargo': (cv2.imread('images/gui/cargo_border_start.png'), every_border_end),
       'drones': (cv2.imread('images/gui/drones_border_start.png'), every_border_end),
       'spots': (cv2.imread('images/gui/spots_border_start.png'), every_border_end)}
