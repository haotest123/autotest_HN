

import unittest
from common.openbrower import KillBrower
from tools.get_driver import GetDriver
from testdatas import comman_datas as CD




class TestMyLogin(unittest.TestCase):

    def setUpClass(cls):
        KillBrower().KillBrower('IE')
        driver=GetDriver.get_web_driver(CD.url_supplier)




















