from sys_pub import *
from ui_pub import *
from struct_pub import *


class Service:
    def __init__(self):
        self._run_title = ''
        self._stop_title = ''
        self._start_title = ''
        self._dir = ''
        self._exe = ''
        self._exe_info = ExeInfo()
        self._status_run = 0
        self._status_stop = 1
        self._status_none = 2
        self._status = self._status_none
        self._start_handle = 0
        self._x = 0
        self._y = 0

    def _init_exe(self):
        self._exe_info.dir = self._dir
        self._exe_info.exe = self._exe

    def _init_status(self):
        handle_ = find_wnd_by_title(self._run_title)
        if 0 != handle_:
            self._exe_info.handle = handle_
            self._status = self._status_run
            return
        handle_ = find_wnd_by_title(self._stop_title)
        if 0 != handle_:
            self._exe_info.handle = handle_
            self._status = self._status_stop

    def _start_app(self, wait=False):
        execute(self._exe_info.path)
        if wait:
            self._exe_info.handle = wait_wnd_run(self._stop_title)
            if not self._exe_info.handle:
                return False
            return True
        else:
            self._exe_info.handle = wait_wnd_run(self._run_title)
            return True

    def _start_service(self, need_click=False):
        if need_click:
            self._start_handle = find_sub_wnd_by_title(self._exe_info.handle, self._start_title)
            if not self._start_handle:
                return False
            click_wnd(self._start_handle)
            return True

    def _move_wnd(self):
        move_wnd(self._exe_info.handle, self._x, self._y)

    def start_service(self):
        self._init_exe()
        self._init_status()
        if self._status_none == self._status:
            self._start_app()
            self._start_service()
            self._move_wnd()
        elif self._status_stop == self._status:
            self._start_service(need_click=True)

    def set_wnd_pos(self, x, y):
        self._x = x
        self._y = y

    def set_run_title(self, title):
        self._run_title = title

    def set_stop_title(self, title):
        self._stop_title = title

    def set_start_title(self, title):
        self._start_title = title

    def set_dir(self, dir_):
        self._dir = dir_

    def set_exe(self, exe):
        self._exe = exe

    def get_main_handle(self):
        return self._exe_info.handle

    def end_app(self):
        os.system('taskkill  /F /IM ' + self._exe_info.exe)

