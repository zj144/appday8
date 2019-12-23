import time

import pytest

from Base.init_driver import contacts_driver
from Page.add_user_page import AddUserPage


class Test_AddUser:
    def setup_class(self):
        self.driver = contacts_driver()
        self.add = AddUserPage(self.driver)

    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture()
    @pytest.mark.parametrize("name,phone",[("张健","16600282792"), ("ch","16600282793")])
    def test_01(self,name,phone):
        self.add.click_add_user()
        self.add.input_user(name,phone)
        time.sleep(3)
        # 按返回键
        self.driver.keyevent(4)

if __name__ == '__main__':
    pytest.main(['test_add_user.py'])