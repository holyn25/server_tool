import inspect
import sys


def file_name(path):
    loc = path.rfind('/')
    if -1 == loc:
        loc = path.rfind('\\')
    if -1 == loc:
        loc = 0
    else:
        loc += 1

    return path[loc:]


def curr_func(level=1):
    return inspect.stack()[level][3]


def log_head(line):
    return '{}() {}:{:d}    '.format(curr_func(3), file_name(__file__), line)


def log_loc():
    print(log_head(sys._getframe().f_back.f_lineno))


def log(log_):
    print("{}{}".format(log_head(sys._getframe().f_back.f_lineno), log_))


