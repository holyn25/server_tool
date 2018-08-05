import time

from pub.sys_pub import *
from pub.ui_pub import *
from pub.struct_pub import *

RUN_TITLE = '协调服务器 -- [ 运行 ]'
STOP_TITLE = '协调服务器 -- [ 停止 ]'
START_TITLE = '启动服务'

STATUS_RUN = 0
STATUS_STOP = 1
STATUS_NONE = 2

corres = ExeInfo()
status = STATUS_NONE

start_handle = 0


def init_exe():
    global corres
    corres.dir = 'd:\\yy\\server\\运行\\Debug\\Unicode\\'
    corres.exe = 'Correspond.exe'
    corres.wnd_title_other = RUN_TITLE
    corres.wnd_title_other = STOP_TITLE


def init_status():
    handle_ = find_window_by_title(RUN_TITLE)
    global status
    status = STATUS_NONE
    if 0 != handle_:
        corres.handle = handle_
        status = STATUS_RUN
        return
    handle_ = find_window_by_title(STOP_TITLE)
    if 0 != handle_:
        corres.handle = handle_
        status = STATUS_STOP


def start_app():
    execute(corres.path)
    corres.handle = wait_wnd_run(STOP_TITLE)
    if not corres.handle:
        return False
    return True


def init_start():
    global start_handle
    global corres
    start_handle = find_sub_window_by_title(corres.handle, START_TITLE)
    if not start_handle:
        return False
    click_window(start_handle)
    start_handle_ = win32gui.FindWindowEx(corres.handle, None, 'RichEdit20A', None)
    for i in range(10):
        time.sleep(1)
        buf_size = win32gui.SendMessage(start_handle_, win32con.WM_GETTEXTLENGTH, 0, 0) + 1  # 要加上截尾的字节
        str_buffer = win32gui.PyMakeBuffer(buf_size)  # 生成buffer对象
        win32api.SendMessage(start_handle_, win32con.WM_GETTEXT, buf_size, str_buffer)  # 获取buffer
        str = str(str_buffer[:-1])
        print(str)

        # buf = win32gui.PyMakeBuffer(100)
        # win32gui.SendMessage(btnhld, win32con.WM_GETTEXT, 100, buf)
        # address, length = PyGetBufferAddressAndLen(buf)
        # text = buf.get(address, length)
        # print('text: ', text)
        pass
    # if txt.endswith('服务启动成功'):
    #         break
    # pass




def test():
    pass


if __name__ == "__main__":
    init_exe()
    init_status()

    if STATUS_NONE == status:
        start_app()
        init_start()
    elif STATUS_STOP == status:
        init_start()

    else:
        pass

    # execute(corres.path)
    # win32gui.GetWindowLongGetWindowLong(hwnd, win32con.SHOWM)
    # win32gui.GetWindowLong(hwnd, win32con.SW_SHOW)
    # win32api.ShellExecute(0, "open", corres.path, '', '', win32con.SW_SHOWNORMAL)
