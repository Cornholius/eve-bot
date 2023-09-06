import os
import shutil


corn812 = {'core_user': 'core_user_6959737.dat', 'core_char': 'core_char_1430237027.dat'}
cornilita_rus = {'core_user': 'core_user_11312363.dat', 'core_char': 'core_char_94768517.dat'}
salman_delpino = {'core_user': 'core_user_14285901.dat', 'core_char': 'core_char_2112215616.dat'}


def clone_ui(folder):
    path = 'C:\\Users\\ylays\\AppData\\Local\\CCP\\EVE\\g_games_eve_sharedcache_tq_tranquility\\settings_' + folder
    try:
        os.remove(f"{path}\\{cornilita_rus['core_user']}")
        os.remove(f"{path}\\{cornilita_rus['core_char']}")
        os.remove(f"{path}\\{salman_delpino['core_user']}")
        os.remove(f"{path}\\{salman_delpino['core_char']}")
    except Exception as error:
        print(error)
    shutil.copyfile(f"{path}\\{corn812['core_user']}", f"{path}\\{cornilita_rus['core_user']}")
    shutil.copyfile(f"{path}\\{corn812['core_char']}", f"{path}\\{cornilita_rus['core_char']}")
    shutil.copyfile(f"{path}\\{corn812['core_user']}", f"{path}\\{salman_delpino['core_user']}")
    shutil.copyfile(f"{path}\\{corn812['core_char']}", f"{path}\\{salman_delpino['core_char']}")


clone_ui('mining')
