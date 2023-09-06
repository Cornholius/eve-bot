import cv2

# общее
screenshot = './images/screenshots/screenshot.png'
every_border_end = cv2.imread('images/gui/every_border_end.png')

# стенды
plus = cv2.imread('images/standings/plus.png')
minus1 = cv2.imread('images/standings/minus1.png')
minus2 = cv2.imread('images/standings/minus2.png')

# цитадели
citadel = {
       'dock': cv2.imread('images/citadel/dock.png'),
       'undock': cv2.imread('images/citadel/undock.png'),
       'dock_spot': cv2.imread('images/citadel/dock_spot.png'),
}

# дроны
drone = {
       'light': cv2.imread('images/drones/light.png'),
       'medium': cv2.imread('images/drones/medium.png'),
       'heavy': cv2.imread('images/drones/heavy.png'),
       'sentry': cv2.imread('images/drones/sentry.png'),
       'launch': cv2.imread('images/drones/launch.png'),
}

# в космосе
space = {
       'establishing_warp': cv2.imread('images/space/establishing.png'),
       'warp_drive_active': cv2.imread('images/space/warp_drive_active.png'),
       'warp': cv2.imread('images/space/warp.png'),
       'warp_to_pkm': cv2.imread('images/space/warp_to_pkm.png'),
       'warp_to_round': cv2.imread('images/space/warp_to_round.png'),
       'spot': cv2.imread('images/citadel/spot.png'),
}

# крабинг
ratting = {
       'squad': cv2.imread('images/ratting/squad.png'),
       'frigate': cv2.imread('images/npc/frigate3.png'),
       'battlecruiser': cv2.imread('images/npc/battlecruiser.png'),
}

# майнинг
mining = {
       'stack_all': cv2.imread('images/mining/stack_all.png'),
       'mining_hold': cv2.imread('images/mining/mining_hold.png'),
       'bonus_cargo': cv2.imread('images/mining/bonus_cargo.png'),
}

# интерфейс
gui = {'overview': (cv2.imread('images/gui/overview_border_start.png'), every_border_end),
       'chat': (cv2.imread('images/gui/chat_border_start.png'),
                cv2.imread('images/gui/chat_border_end.png')),
       'cargo': (cv2.imread('images/gui/cargo_border_start.png'),
                 cv2.imread('images/gui/cargo_border_end.png')),
       'drones': (cv2.imread('images/gui/drones_border_start.png'), every_border_end),
       'spots': (cv2.imread('images/gui/spots_border_start.png'), every_border_end),
       'probe_scanner': (cv2.imread('images/gui/probe_scanner_border_start.png'),
                         cv2.imread('images/gui/probe_scanner_border_end.png'))
       }
