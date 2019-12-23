'''
封装公共操作
将定位每一个元素都封装为显式等待

'''
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    def find_elements(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))

    # 调用上面方法，执行元素相关操作
    def click_element(self,el,timeout=10,poll=0.5):
        self.find_element(el,timeout,poll).click()

    def input_text(self,el,text,timeout=10,poll=0.5):
        input = self.find_element(el,timeout,poll)
        input.clear()
        input.send_keys(text)
