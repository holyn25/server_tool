import win32gui
import win32api
import win32con


def get_window_by_txt(txt):
    handle_loc = win32gui.FindWindow(0, txt)
    print(handle_loc)
    return handle_loc


def get_sub_window_by_txt(handle_par, txt):
    handle_loc = win32gui.FindWindowEx(handle_par, None, None, txt)
    print(handle_loc)
    return handle_loc


def get_window_by_class(class_par):
    handle_loc = win32gui.FindWindow(class_par, '')
    print(handle_loc)
    return handle_loc


def get_window_txt(handle_par):
    txt = win32gui.GetWindowText(handle_par)
    print(txt)
    return txt


def click_window(handle_par):
    win32gui.SendMessage(handle_par, win32con.WM_LBUTTONDOWN, 0, 0);
    win32gui.SendMessage(handle_par, win32con.WM_LBUTTONUP, 0, 0);


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
