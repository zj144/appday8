import os
import sys

import pytest

sys.path.append(os.getcwd()) #将脚本路径添加到python搜索路径
from Base.init_driver import init_driver
from Base.page import Page_Obj


'''
点击移动网络设置页面
'''
class TestsetMoble():
    def setup_class(self):
        self.driver = init_driver()
        # self.set_page = SetPage(self.driver)
        # self.more_page = SetMorepage(self.driver)
        # self.set_mob = SetmoblePage(self.driver)
        self.obj = Page_Obj(self.driver)
    def teardown_class(self):
        self.driver.quit()
    # 初始化操作
    @pytest.fixture(scope='class',autouse=True)
    def goto_set_mb(self):
        self.obj.get_set_page().set_page.click_more()
        self.obj.set_moble_page().click_mobile()
    @pytest.mark.parametrize('a',['2G','3G'])
    def test_set_mb(self,a):
        self.obj.set_moble_page().click_first_mob()
        self.obj.set_moble_page().click_2g(a)
        ss =  self.obj.set_moble_page().get_summary()
        assert a in ss

if __name__ == '__main__':
    pytest.main(['test_set_moble.py'])