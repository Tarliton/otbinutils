from otbinutils.fileutils import fileutils

class TSpr():
    def __init__(self, version):
        self.version = version
        self.file = fileutils.File(version, "spr")