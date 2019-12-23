import time

import pytest

from Base.init_driver import contacts_driver
from Page.add_user_page import AddUserPage, SetUserPage


class Test_AddUser:
    def setup_class(self):
        self.driver = contacts_driver()
        self.add = AddUserPage(self.driver)
        self.set = SetUserPage(self.driver)

    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture()
    def click_user1(self):
        self.driver.find_element_by_id('com.android.contacts:id/cliv_name_textview').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.android.contacts:id/menu_edit').click()
        time.sleep(3)
    @pytest.mark.parametrize("name",[("python"), ("appium"),('selenium')])
    def test_01(self,click_user1,name):
        self.set.input_user(name)
        time.sleep(3)

        try:
            self.driver.find_element_by_xpath("//*[contains(@text,{})]".format(name))
            assert True
        except:
            assert False

        # 按返回键
        self.driver.keyevent(4)


if __name__ == '__main__':
    pytest.main(['test_set_user.py'])