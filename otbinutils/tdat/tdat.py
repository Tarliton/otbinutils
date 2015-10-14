from otbinutils.fileutils import fileutils

class TDat():
    def __init__(self, version):
        self.version = version
        self.file = fileutils.File(version, "dat")

    def to_json(self):
    	pass