from Base.Base import Base
from Page.pageElements import SearchElements

'''
更多页面元素操作封装
'''


class SetMorepage(Base):
    # 将驱动对象传入父类
    def __init__(self,driver):
        Base.__init__(self,driver)

    # 点击移动网络
    def click_mobile(self):
        self.click_element(SearchElements.more_mobile_xpath)

