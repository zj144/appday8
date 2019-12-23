from selenium.webdriver.common.by import By


class SearchElements():

    # 通讯录页面元素




    '''设置页面元素'''
    # 点击搜索
    click_se = (By.ID, "com.android.settings:id/search")
    # 点击wlan
    click_wl_xpath = (By.XPATH,"//*[contains(@text,'WLAN')]")
    # 蓝牙
    # 更多
    more_xpath = (By.XPATH,"//*[contains(@text,'更多')]")
    # 显示
    # 提示通知
    # 存储
    # 电池
    # 应用
    # 应用兼容
    # 电池



    ''' 点击设置搜索页面'''
    # 搜索框输入
    send_keys = (By.ID, "android:id/search_src_text")
    # 获取搜索到的结果
    get_rs = (By.ID, "com.android.settings:id/title")


    '''更多页面'''
    # 移动网络
    more_mobile_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")

    '''移动网络设置'''

    # 点击首选网络类型
    mobile_first_mobile=(By.XPATH, "//*[contains(@text,'首选网络')]")
    # 2g
    mobile_select_2G_btn_xpath = (By.XPATH, "//*[contains(@text,'2G')]")
    # 3g
    mobile_select_3G_btn_xpath = (By.XPATH, "//*[contains(@text,'3G')]")

    # 所有选中的网络类型
    mobile_get_summary_text_ids = (By.ID, "android:id/summary")

    # mobile_quit_summary = (By.XPATH, "//*[contains(@text,'取消')]")

    '''
    添加联系人页面元素
    '''
    # 点击新增联系人
    add_user_button = (By.ID, "com.android.contacts:id/floating_action_button")
    # 输入姓名
    input_name = (By.XPATH, "//*[contains(@text,'姓名')]")
    # 输入电话
    input_phone = (By.XPATH, "//*[contains(@text,'电话')]")
