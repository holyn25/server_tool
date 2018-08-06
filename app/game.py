from service_base import *


class Game(Service):
    def __init__(self):
        super(Game, self).__init__()
        self._load_title = '加载房间'

    def get_load_title(self):
        return self._load_title


def init_game(game_):
    game_.set_dir('d:\\yy\\server\\运行\\Debug\\Unicode\\')
    game_.set_exe('GameServer.exe')
    game_.set_run_title('游戏服务器 -- [ 运行 ]')
    game_.set_stop_title('游戏服务器 -- [ 停止 ]')
    game_.set_wnd_pos(50, 50)


def flow():
    game = Game()
    init_game(game)
    main_handle = find_window_by_title('游戏服务器 -- [ 停止 ]')
    sub_handle = find_sub_window_by_title(main_handle, game.get_load_title())


if __name__ == "__main__":
    flow()


