import win32api
import win32gui

import win32con


def execute(path):
    win32api.WinExec(path, win32con.SW_SHOWNORMAL)


def msg_box(title, txt):
    win32gui.MessageBox(0, txt, title, win32con.MB_OK)
