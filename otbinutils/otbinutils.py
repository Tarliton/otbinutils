from otbinutils.tdat import tdat
from otbinutils.tspr import tspr


class OtBinUtils():
    def __init__(self, version):
        self.t_dat = tdat.TDat(version)
        self.t_spr = tspr.TSpr(version)
