import os
import sys

import pytest

sys.path.append(os.getcwd()) #将脚本路径添加到python搜索路径
from selenium.webdriver.common.by import By

from Base.Base import Base
from Base.init_driver import init_driver
from Page.set_search_page import SetPage


class TestSetsearch():
    def setup_class(self):
        self.driver = init_driver()
        self.page = SetPage(self.driver)
    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class',autouse=True)
    def goto_search(self):
        self.page.click_serch()

    @pytest.mark.parametrize("d,c",[("1","休眠")])
    def test_01set_search(self,d,c):
        self.page.send_search(d)
        assert c in self.page.get_search_result()

if __name__ == '__main__':
    pytest.main(['test_set_search.py'])

