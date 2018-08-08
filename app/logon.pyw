from service_base import *
import os


def _init(service_):
    service_.set_dir('d:\\yy\\server\\运行\\Debug\\Unicode\\')
    service_.set_exe('LogonServer.exe')
    service_.set_run_title('登录服务器 -- [ 运行 ]')
    service_.set_stop_title('登录服务器 -- [ 停止 ]')
    service_.set_start_title('启动服务')
    service_.set_wnd_pos(2400, 90)


def flow():
    service = Service()
    _init(service)
    service.start_service()


def end_app():
    exit_exe('LogonServer.exe')


if __name__ == "__main__":
    flow()
