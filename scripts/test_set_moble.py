import pytest
from selenium.webdriver.common.by import By

from Base.init_driver import init_driver
from Page.more_page import SetMorepage
from Page.set_mobile_page import SetmoblePage
from Page.set_search_page import SetPage

'''
点击移动网络设置页面
'''
class TestsetMoble():
    def setup_class(self):
        self.driver = init_driver()
        self.set_page = SetPage(self.driver)
        self.more_page = SetMorepage(self.driver)
        self.set_mob = SetmoblePage(self.driver)
    def teardown_class(self):
        self.driver.quit()
    # 初始化操作
    @pytest.fixture(scope='class',autouse=True)
    def goto_set_mb(self):
        self.set_page.click_more()
        self.more_page.click_mobile()
    @pytest.mark.parametrize('a',['2G','3G'])
    def test_set_mb(self,a):
        self.set_mob.click_first_mob()
        self.set_mob.click_2g(a)
        ss =  self.set_mob.get_summary()
        assert a in ss

if __name__ == '__main__':
    pytest.main(['test_set_moble.py'])