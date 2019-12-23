'''
通讯录页面公共数据

'''
'''
#点击添加用户数据
'''

from selenium.webdriver.common.by import By

add_user_button = (By.ID,"com.android.contacts:id/floating_action_button")

input_name = (By.XPATH,"//*[contains(@text,'姓名')]")
input_phone = (By.XPATH,"//*[contains(@text,'电话')]")
input_back = (By.XPATH,"//*[contains(@class,'android.widget.ImageButton')]")


'''
点击修改用户
'''
input_setphone = (By.CLASS_NAME,"android.widget.EditText")
input_setback = (By.XPATH,"//*[contains(@class,'android.widget.ImageButton')]")


'''
设置搜索页元素
'''

