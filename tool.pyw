from service_base import *
import os


class Game(Service):
    def __init__(self):
        super(Game, self).__init__()
        self._exe_info.dir = 'd:\\yy\\resource\\'
        self._exe_info.exe = 'GameCityPCTools.exe'
        self._exe_info.wnd_title = 'GameCityPC'
        self._title_open = '开启客户端'
        self._title_close = '关闭客户端'
        self._title_city = '电玩城'
        self._handle_city = 0
        if is_s_screen():
            self._x = 1000
        else:
            self._x = 3420
        self._y = 100

        if is_s_screen():
            self._x_city = 1000
        else:
            self._x_city = 2000
        self._y_city = 200

    def _wait_city(self):
        self._handle_city = wait_wnd_run(self._title_city)
        if self._handle_city:
            return True
        return False

    def _open_city(self):
        handle_open = find_sub_wnd_by_title(self._exe_info.handle, self._title_open)
        if not handle_open:
            return False
        click_wnd(handle_open)

    def _close_city(self):
        handle_close = find_sub_wnd_by_title(self._exe_info.handle, self._title_close)
        if not handle_close:
            return False
        click_wnd(handle_close)
        time.sleep(1)

    def _start_app(self):
        execute(self._exe_info.path)
        self._exe_info.handle = wait_wnd_run(self._exe_info.wnd_title)
        if not self._exe_info.handle:
            return False
        return True

    def _init_status(self):
        self._exe_info.handle = find_wnd_by_title(self._exe_info.wnd_title)
        if 0 != self._exe_info.handle:
            self._status = self._status_run

    def _move_city(self):
        move_wnd(self._handle_city, self._x_city, self._y_city)

    def start(self):
        self._init_status()
        if self._status_none == self._status:
            self._start_app()
            self._move_wnd()
            self._open_city()
        else:
            self._close_city()
            self._open_city()
        if not self._wait_city():
            return
        self._move_city()


def flow():
    game = Game()
    game.start()


def end_app():
    exit_exe('GameCityPCTools.exe')


if __name__ == "__main__":
    flow()
