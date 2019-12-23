from appium import webdriver
from selenium.webdriver.common.by import By

'''
设置页面元素操作封装
'''

from Base.Base import Base
from Base.init_driver import init_driver
from Page.pageElements import SearchElements


'''
设置页面操作封装
'''


class SetPage(Base):
    # 继承父类，将driver对象传到父类
    def __init__(self,driver1):
        Base.__init__(self,driver1)

    def click_serch(self):
        self.click_element(SearchElements.click_se)

    def send_search(self,text):
        self.input_text(SearchElements.send_keys,text)

    def get_search_result(self):
        result =self.find_elements(SearchElements.get_rs)
        return [x.text for x in result]

    # 点击更多
    def click_more(self):
        self.click_element(SearchElements.more_xpath)





# ss = SetPage(init_driver())
# ss.click_serch()





