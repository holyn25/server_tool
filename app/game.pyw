from service_base import *


class Game(Service):
    def __init__(self):
        super(Game, self).__init__()
        self._load_title = '加载房间'
        self._load_handle = 0

    def _load(self):
        self._load_handle = find_sub_window_by_title(self._exe_info.handle, self._load_title)
        if not self._load_handle:
            return False
        click_window(self._load_handle)
        log(self._load_handle)

    def start_service(self):
        self._init_exe()
        self._init_status()

        if self._status_none == self._status:
            self._start_app()
            self._move_wnd()
            self._load()
        elif self._status_stop == self._status:
            self._load()


def init_game(game_):
    game_.set_dir('d:\\yy\\server\\运行\\Debug\\Unicode\\')
    game_.set_exe('GameServer.exe')
    game_.set_run_title('游戏服务器 -- [ 运行 ]')
    game_.set_stop_title('游戏服务器 -- [ 停止 ]')
    game_.set_wnd_pos(2850, 90)


def flow():
    game = Game()
    init_game(game)
    game.start_service()


if __name__ == "__main__":
    flow()


