'''
移动网络设置页面元素操作封装
'''
from Base.Base import Base
from Page.pageElements import SearchElements


class SetmoblePage(Base):
    # 将驱动对象传到父类当中
    def __init__(self,driver):
        Base.__init__(self,driver)
    # 点击首选网络类型
    def click_first_mob(self):
        self.click_element(SearchElements.mobile_first_mobile)
    # 点击2g
    def click_2g(self,a="2G"):
        if a == "2G":
            self.click_element(SearchElements.mobile_select_2G_btn_xpath)
        else:
            self.click_element(SearchElements.mobile_select_3G_btn_xpath)
    # 获取所有选中的网络类型
    def get_summary(self):
        result = self.find_elements(SearchElements.mobile_get_summary_text_ids)
        return [x.text for x in result]

