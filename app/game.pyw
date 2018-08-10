from service_base import *
import os


class Game(Service):
    def __init__(self):
        super(Game, self).__init__()
        self._load_title = '加载房间'
        self._load_handle = 0
        self._room_tile = '房间列表'
        self._room_handle = 0
        self._list_cls = 'SysListView32'
        self._list_handle = 0
        self._list_x = 100
        self._list_y = 21
        self._list_item_high = 17.875
        self._room_slct = -1

    def set_room_slct(self, item):
        self._room_slct = item

    def _load(self):
        self._load_handle = find_sub_wnd_by_title(self._exe_info.handle, self._load_title)
        if not self._load_handle:
            return False
        click_wnd(self._load_handle)

    def _wait_room(self):
        self._room_handle = wait_wnd_run(self._room_tile)
        if self._room_handle:
            return True
        return False

    def _slct_room(self):
        if -1 == self._room_slct:
            return
        # self._list_handle = find_sub_wnd_by_cls(self._room_handle, self._list_cls)
        left, top, right, bottom = win32gui.GetWindowRect(self._room_handle)
        time.sleep(3)
        x = left + self._list_x
        y = top + int((1 + self._room_slct) * self._list_item_high)
        d_click_mouse(x, y)

    def _launch(self):
        time.sleep(2)
        self._start_handle = find_sub_wnd_by_title(self._exe_info.handle, self._start_title)
        if not self._start_handle:
            return False
        click_wnd(self._start_handle)

    def _start_app(self):
        execute_mt(self._exe_info.path)
        self._exe_info.handle = wait_wnd_run(self._stop_title)
        if not self._exe_info.handle:
            return False
        return True

    def start_service(self):
        self._init_exe()
        self._init_status()

        if self._status_none == self._status:
            self._start_app()
            self._move_wnd()
            self._load()
        elif self._status_stop == self._status:
            self._load()

        if not self._wait_room():
            return

        # self._slct_room()
        # self._launch()


def init_game(game_):
    game_.set_dir('d:\\yy\\server\\运行\\Debug\\Unicode\\')
    game_.set_exe('GameServer.exe')
    game_.set_run_title('游戏服务器 -- [ 运行 ]')
    game_.set_stop_title('游戏服务器 -- [ 停止 ]')
    game_.set_start_title('启动服务')
    # game_.set_wnd_pos(2850, 90)
    game_.set_wnd_pos(100, 90)
    game_.set_room_slct(0)


def flow():
    game = Game()
    init_game(game)
    game.start_service()


def end_app():
    exit_exe('GameServer.exe')


if __name__ == "__main__":
    flow()


