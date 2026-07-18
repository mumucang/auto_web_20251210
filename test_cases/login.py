import os
import time

import allure
import pytest

from config import datas_path
from pages.base_pages import BasePage
from pages.login_page import LoginPage
from utils.read_excle_util import ReadExcelUtil

datas = ReadExcelUtil.read_excle(os.path.join(datas_path, 'ecshop_datas.xlsx'), "login_data")

@allure.feature("登录模块")
@allure.story("登录")
class TestLogin:

    def setup_method(self):
        self.login_page = LoginPage()
        self.login_page.open_page(self.login_page.login_url)

    def teardown_method(self):
        time.sleep(1)
        self.login_page.take_screenshot(LoginPage.__name__)
        self.login_page.close_page()

    @pytest.mark.parametrize("biaoti,username, password,qiwangjieguo", datas)
    @allure.title("{biaoti}登录测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self,biaoti,username, password,qiwangjieguo):

        # if username =="" or password =="":
        #     self.login_page.login(username, password)
        #     text = self.login_page.login_failer()
        # else:
        #     self.login_page.login(username, password)
        #     text = self.login_page.login_success()

        with allure.step("登录操作"):
            self.login_page.login(username, password)
        with allure.step("验证是否登录成功"):
            try:
                text = self.login_page.login_failer()
            except Exception as e:
                text = self.login_page.login_success()
            assert qiwangjieguo in text

        # try:
        #     self.login_page.login(username, password)
        #     text = self.login_page.login_failer()
        #
        # except Exception as e:
        #     text = self.login_page.login_success()







