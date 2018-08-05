class ExeInfo(object):
    def __init__(self):
        self._exe = ''
        self._dir = ''
        self._handle = 0
        self._wnd_title = ''
        self._wnd_title_other = []

    @property
    def handle(self):
        return self._handle

    @handle.setter
    def handle(self, handle_):
        self._handle = handle_

    @property
    def wnd_title(self):
        return self._wnd_title

    @wnd_title.setter
    def wnd_title(self, title):
        self._wnd_title = title

    @property
    def exe(self):
        return self._exe

    @exe.setter
    def exe(self, exe):
        self._exe = exe

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, dir_):
        self._dir = dir_

    @property
    def path(self):
        return self._dir + self._exe

    @property
    def wnd_title_other(self):
        return self._wnd_title_other

    @wnd_title_other.setter
    def wnd_title_other(self, title):
        if 0 == self._wnd_title_other.count(title):
            self._wnd_title_other.append(title)
