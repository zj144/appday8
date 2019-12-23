'''
定义统一入口类
实例化所有页面驱动返回
'''
from Base.Base import Base
from Page.more_page import SetMorepage
from Page.set_mobile_page import SetmoblePage
from Page.set_search_page import SetPage
'''
定义方法返回实例化好的页面对象
'''

class Page_Obj(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 返回设置页面
    def get_set_page(self):
        return SetPage(self.driver)
    # 返回更多
    def get_more_page(self):
        return SetMorepage(self.driver)
    # 返回移动网络
    def set_moble_page(self):
        return SetmoblePage(self.driver)