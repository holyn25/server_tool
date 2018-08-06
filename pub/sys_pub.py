import time
import win32api
import win32gui
import win32con
import win32com.client
from pub.base_pub import *
from pub.ui_pub import *


def execute(path):
    log(path)
    if not is_run(file_name(path)):
        win32api.ShellExecute(0, "open", path, '', '', win32con.SW_SHOWNORMAL)


def msg_box(txt, title='提示'):
    win32gui.MessageBox(0, txt, title, win32con.MB_OK)


def is_run(process_name_):
    if -1 == process_name_.find('.'):
        process_name = process_name_ + '.exe'
    else:
        process_name = process_name_
    service = win32com.client.Dispatch('WbemScripting.SWbemLocator')
    server = service.ConnectServer('127.0.0.1', 'root\cimv2', '', '')
    ps = server.ExecQuery('select * from Win32_Process')
    found = False
    for p in ps:
        if p.Name.upper() == process_name.upper():
            found = True
            break
    del service
    return found


def wait_wnd_run(title, wait=10):
    handle_ = 0
    for i in range(wait):
        handle_ = find_window_by_title(title)
        if handle_:
            return handle_
        time.sleep(1)
    msg_box('failure to find {}'.format(title))
    return handle_
