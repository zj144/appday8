# 打开设置，打开通讯录

from appium import webdriver
def init_driver():
    desired = {
        "platformName": "android",
        "platformVersion": "5.1",
        # "deviceName": "192.168.94.101:5555",
        # "deviceName": "emulator-5554",
        # 夜神
        "deviceName": "127.0.0.1:62001",
        "appActivity": ".Settings",
        "appPackage": "com.android.settings",
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)
    return driver

def contacts_driver():
    desired = {
        "platformName": "android",
        "platformVersion": "5.1",
        # "deviceName": "192.168.94.101:5555",
        "deviceName": "emulator-5554",
        "appActivity": ".activities.PeopleActivity",
        "appPackage": "com.android.contacts",
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)
    return driver


