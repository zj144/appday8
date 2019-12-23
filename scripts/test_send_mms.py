import os
import sys

import pytest
sys.path.append(os.getcwd()) #将脚本路径添加到python搜索路径
import time
from Base.init_driver import text_driver
from Base.page import Page_Obj
class TestsendMms:
    def setup_class(self):
        self.driver = text_driver()
        self.obj = Page_Obj(self.driver)
    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture(autouse=True)
    def goto_mms(self):
        self.obj.send_mms().click_new_mms()
    @pytest.mark.parametrize('a,b',[('13689342491','勒布朗詹姆斯'),('16600282792','库里'),('16612345678','浓眉')])
    def test_new_mms(self,a,b):
        self.obj.send_mms().send_mms(a,b)
        rs = self.obj.send_mms().get_mms_rs()
        assert b in rs
        self.obj.send_mms().mms_back()
        time.sleep(3)

if __name__ == '__main__':
    pytest.main(['test_send_mms.py'])