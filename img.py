import cv2

# общее
screenshot = cv2.imread('./images/screenshot.png')

# стенды
plus = cv2.imread('images/standings/standings/plus.png')
minus1 = cv2.imread('images/standings/standings/minus1.png')
minus2 = cv2.imread('images/standings/standings/minus2.png')

# цитадели
dock = cv2.imread('images/citadel/dock.png')
undock = cv2.imread('images/citadel/undock.png')
astrahaus = cv2.imread('images/citadel/astrahaus.png')
raitaru = cv2.imread('images/citadel/raitaru.png')
fortizar = cv2.imread('images/citadel/fortizar.png')

# в космосе
warping = cv2.imread('images/space/warping.png')
warp_drive_active = cv2.imread('images/space/warp_drive_active.png')
spot = cv2.imread('images/space/spot.png')
warp = cv2.imread('images/space/warp.png')

gui = {'overview': (cv2.imread('images/gui/overview_border_start.png'), cv2.imread(
       'images/gui/overview_border_end.png')),
       'chat': (cv2.imread('images/gui/chat_border_start.png'), cv2.imread('images/gui/chat_border_end.png')),
       'cargo': (cv2.imread('images/gui/cargo_border_start.png'), cv2.imread('images/gui/cargo_border_end.png')),
       'drones': (cv2.imread('images/gui/drones_border_start.png'), cv2.imread('images/gui/drones_border_end.png')),
       'spots': (cv2.imread('images/gui/spots_border_start.png'), cv2.imread('images/gui/spots_border_end.png'))}
