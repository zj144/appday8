'''
通讯录页面操作封装
'''
import time

import Page
from Base.Base import Base


class AddUserPage(Base):
    # 继承父辈方法，将驱动对象传到父类方法中
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_add_user(self):
        self.click_element(Page.add_user_button)

    def input_user(self,name,phone):
        self.input_text(Page.input_name,name)
        self.input_text(Page.input_phone,phone)
        time.sleep(3)
        self.click_element(Page.input_back)
        time.sleep(3)



class SetUserPage(Base):
    # 继承父辈方法，将驱动对象传到父类方法中
    def __init__(self,driver):
        Base.__init__(self,driver)

    def input_user(self,name):
        self.input_text(Page.input_setphone,name)
        time.sleep(6)
        self.click_element(Page.input_back)
        time.sleep(3)


