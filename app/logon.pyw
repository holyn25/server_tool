from service_base import *


def flow():
    service = Service()
    service.set_dir('d:\\yy\\server\\运行\\Debug\\Unicode\\')
    service.set_exe('LogonServer.exe')
    service.set_run_title('登录服务器 -- [ 运行 ]')
    service.set_stop_title('登录服务器 -- [ 停止 ]')
    service.set_start_title('启动服务')
    service.set_wnd_pos(2400, 90)
    service.start_service()


if __name__ == "__main__":
    flow()
