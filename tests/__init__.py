import unittest
from otbinutils.tdat import tdat


class TDatTestCase(unittest.TestCase):

    def setUp(self):
        self.t_dat = tdat.TDat(1076)

    def test_to_json(self):
        self.t_dat.to_json()
