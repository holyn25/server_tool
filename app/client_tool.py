from pub.ui_pub import *
import time


clientGameTxt = '电玩城'

clientToolTxt = 'MajoPCTools'
clientToolCls = 'WindowsForms10.Window.8.app.0.141b42a_r12_ad1'
clientToolName = "MajoPCTools.exe"
clientToolDir = "d:\\yy\\resource\\"
clientToolPath = clientToolDir + clientToolName;

startClientTxt = '开启客户端'

if __name__ == "__main__":
    open(clientToolPath)
    time.sleep(1)
    handle_tool = find_window_by_title(clientToolTxt)
    move_window(handle_tool, 3300, 100)
    handle_start = find_sub_window_by_title(handle_tool, startClientTxt)
    click_window(handle_start)
    time.sleep(1)
    handle_game = find_window_by_title(clientGameTxt)
    move_window(handle_game, 2000, 100)

