import allure
import pytest


class Test_003:

    # @allure.step("这是一个测试步骤~")
    # def test_003_1(self):
    #     allure.attach("文件名称","文件内容，具体步骤描述信息")
    #     assert True
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_01(self):
        assert True
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_02(self):
        assert True
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_03(self):
        assert True
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_04(self):
        assert False
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_05(self):
        assert True