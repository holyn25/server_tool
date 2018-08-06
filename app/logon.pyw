from pub.sys_pub import *
from pub.ui_pub import *
from pub.struct_pub import *


RUN_TITLE = '登录服务器 -- [ 运行 ]'
STOP_TITLE = '登录服务器 -- [ 停止 ]'
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
    corres.exe = 'LogonServer.exe'
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


def start_service():
    global start_handle
    global corres
    start_handle = find_sub_window_by_title(corres.handle, START_TITLE)
    if not start_handle:
        return False
    click_window(start_handle)
    # txt_handle_ = win32gui.FindWindowEx(corres.handle, None, 'RichEdit20A', None)
    # log(txt_handle_)
    # for i in range(5):
    #     time.sleep(1)
    #     txt = get_dlg_txt(txt_handle_)
    #     log(txt)
    #     if not txt.endswith('服务启动成功'):
    #         log(txt)
    #         return
    # msg_box('启动服务失败')


def set_wnd_pos():
    move_window(corres.handle, 2400, 20)


def flow():
    init_exe()
    init_status()
    if STATUS_NONE == status:
        start_app()
        start_service()
        set_wnd_pos()
    elif STATUS_STOP == status:
        start_service()


if __name__ == "__main__":
    flow()

