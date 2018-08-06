import win32gui
import win32api
import win32con


def find_window_by_title(title):
    handle_ = win32gui.FindWindow(0, title)
    print(handle_)
    return handle_


def find_sub_window_by_title(handle_par, title):
    handle_ = win32gui.FindWindowEx(handle_par, None, None, title)
    print(handle_)
    return handle_


def find_window_by_class(class_par):
    handle_ = win32gui.FindWindow(class_par, '')
    print(handle_)
    return handle_


def get_window_txt(handle_par):
    txt = win32gui.GetWindowTextwin32gui.GetWindowText(handle_par)
    print(txt)
    return txt


def click_window(handle_par):
    win32gui.SendMessage(handle_par, win32con.WM_LBUTTONDOWN, 0, 0)
    win32gui.SendMessage(handle_par, win32con.WM_LBUTTONUP, 0, 0)


def close_window(handle_par):
    # win32gui.CloseWindow(handle_par)
    win32api.SendMessage(handle_par, win32con.WM_CLOSE, 0, 0)


def move_mouse(x, y):
    x_loc, y_loc = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.SetCursorPos((x_loc, y_loc))


def move_window(handle_par, x, y):
    left, top, right, bottom = win32gui.GetWindowRect(handle_par)
    win32gui.MoveWindow(handle_par, x, y, right-left, bottom-top, False)


def wnd_enum(hwnd, rslt_list):
    rslt_list.append((hwnd, win32gui.GetWindowText(hwnd), win32gui.GetClassName(hwnd)))


def wnd_child_enum(hwnd, rslt_list):
    rslt_list.append((hwnd, win32gui.GetWindowText(hwnd), win32gui.GetClassName(hwnd)))


def enum_all_child_wnd(handle, rslt_list, level):
    handle_list = []
    if 0 == level:
        return
    # noinspection PyBroadException
    try:
        rslt_list.append((handle, win32gui.GetClassName(handle), win32gui.GetWindowText(handle)))
        win32gui.EnumChildWindows(handle, wnd_child_enum, handle_list)
        for cw in handle_list:
            enum_all_child_wnd(cw[0], rslt_list, level - 1)
    except Exception:
        pass


def enum_all_wnd(level=2):
    top_wnd = []
    win32gui.EnumWindows(wnd_enum, top_wnd)
    find_rslt = []
    # noinspection PyBroadException
    try:
        for wnd in top_wnd:
            handle = wnd[0]
            enum_all_child_wnd(handle, find_rslt, level)
    except Exception:
        pass
    return find_rslt


class WndInfo:
    def __init__(self, handle_=0, title_='', cls_=''):
        self._handle = handle_
        self._title = title_
        self._cls = cls_

    @property
    def handle(self):
        return self._handle

    @handle.setter
    def handle(self, handle_):
        self._handle = handle_

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_):
        self._title = title_

    @property
    def cls(self):
        return self._cls

    @cls.setter
    def cls(self, cls_):
        self._cls = cls_


def get_top_wnd_list():
    wnd_list = []
    win32gui.EnumWindows(lambda wnd_, param: param.append(wnd_), wnd_list)
    return wnd_list


def get_dlg_txt(handle_):
    buf_size = win32gui.SendMessage(handle_, win32con.WM_GETTEXTLENGTH, 0, 0) + 1  # 要加上截尾的字节
    str_buffer = win32gui.PyMakeBuffer(buf_size)  # 生成buffer对象
    win32api.SendMessage(handle_, win32con.WM_GETTEXT, buf_size, str_buffer)  # 获取buffer
    address, length = win32gui.PyGetBufferAddressAndLen(str_buffer)
    return win32gui.PyGetString(address, length)
