from Base.Base import Base
from Page.pageElements import SearchElements


class MmsfPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_new_mms(self):
        self.click_element(SearchElements.new_ms_id)

    def send_mms(self,a,b):
        self.input_text(SearchElements.mms_use_xp,a)
        self.input_text(SearchElements.mms_send_xp,b)
        self.click_element(SearchElements.mms_click_send)
    def get_mms_rs(self):

        ss = self.find_elements(SearchElements.mms_result)
        return [x.text for x in ss]
    def mms_back(self):
        self.click_element(SearchElements.mms_back)






