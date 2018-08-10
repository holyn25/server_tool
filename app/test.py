import win32api
import win32gui
import win32con
import threading


def run():
    print('a')


t1 = threading.Thread(target=run)
t1.start()


