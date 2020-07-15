import cv2

# общее
screenshot = cv2.imread('./images/screenshot.png')

# стенды
plus = cv2.imread('./images/plus.png')
minus1 = cv2.imread('./images/minus1.png')
minus2 = cv2.imread('./images/minus2.png')

# цитадели
dock = cv2.imread('./images/dock.png')
undock = cv2.imread('./images/undock.png')
astrahaus = cv2.imread('./images/astrahaus.png')
raitaru = cv2.imread('./images/raitaru.png')
fortizar = cv2.imread('./images/fortizar.png')

# в космосе
warping = cv2.imread('./images/warping.png')
warp_drive_active = cv2.imread('./images/warp_drive_active.png')
overview_border_start = cv2.imread('./images/overview_border_start.png')
overview_border_end = cv2.imread('./images/overview_border_end.png')
spot = cv2.imread('./images/spot.png')
warp = cv2.imread('./images/warp.png')

gui = {'overview': (cv2.imread('./images/overview_border_start.png'), cv2.imread('./images/overview_border_end.png')),
       'chat': (cv2.imread('./images/chat_border_start.png'), cv2.imread('./images/chat_border_end.png')),
       'cargo': (cv2.imread('./images/cargo_border_start.png'), cv2.imread('./images/cargo_border_end.png')),
       'drones': (cv2.imread('./images/drones_border_start.png'), cv2.imread('./images/drones_border_end.png')),
       'spots': (cv2.imread('./images/spots_border_start.png'), cv2.imread('./images/spots_border_end.png'))}
