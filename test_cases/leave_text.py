import os.path
import time

import allure
import pytest

from config import datas_path
from pages.my_leave_text import MyLeaveTextPage
from utils.read_excle_util import ReadExcelUtil

leave_text_datas = ReadExcelUtil.read_excle(os.path.join(datas_path,"ecshop_datas.xlsx"),"leave_text_data")

@allure.feature("我的留言")
@allure.story("留言功能")
class TestLeaveText:

    def teardown_method(self):

        self.leave_text_page.take_screenshot(MyLeaveTextPage.__name__)
        self.leave_text_page.close_page()

    @pytest.mark.parametrize("title,msg_title,msg_content,result",leave_text_datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_leave_text_success(self,my_account,title,msg_title,msg_content,result):

        with allure.step("留言"):
            my_account.click_my_account()
            my_account.click_my_leave_text()
            self.leave_text_page = MyLeaveTextPage(my_account.driver)
            self.leave_text_page.submit_leave_text(msg_title, msg_content)
        with allure.step("验证留言"):
            try:
                text = self.leave_text_page.submit_leave_text_failer()
            except Exception as e:
                time.sleep(2)
                text = self.leave_text_page.submit_leave_text_success()
            assert result in text



    # def test_leave_text_nonetitle_failer(self,my_account):
    #     my_account.click_my_account()
    #     my_account.click_my_leave_text()
    #     self.leave_text_page = MyLeaveTextPage(my_account.driver)
    #     self.leave_text_page.submit_leave_text("", "自动化测试")