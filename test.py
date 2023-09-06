import win32con
import win32gui
from time import sleep
import win32com.client
import win32con

corn = win32gui.FindWindow(None, 'EVE - Corn812')
cornilita = win32gui.FindWindow(None, 'EVE - Cornilita Rus')
salman = win32gui.FindWindow(None, "EVE - Salman Del'Pino")
# shell = win32com.client.Dispatch("WScript.Shell")

win32gui.SetForegroundWindow(cornilita)
sleep(3)
win32gui.ShowWindow(corn, win32con.SW_MAXIMIZE)
sleep(2)
win32gui.ShowWindow(corn, win32con.SW_MINIMIZE)
sleep(2)
win32gui.ShowWindow(salman, win32con.SW_MAXIMIZE)
sleep(2)
win32gui.ShowWindow(salman, win32con.SW_MINIMIZE)
# shell.SendKeys('alt')
# win32gui.SetForegroundWindow(corn)
# sleep(3)
# shell.SendKeys('alt')
# win32gui.SetForegroundWindow(salman)
