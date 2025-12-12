import random

from selenium.webdriver.common.by import By

from pages.base_pages import BasePage


class MyLeaveTextPage(BasePage):

    leave_type_ele=(By.NAME,'msg_type')
    msg_title_ele=(By.NAME,'msg_title')
    msg_content_ele=(By.NAME,'msg_content')
    submit_btn_ele=(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/form/table/tbody/tr[5]/td[2]/input[2]')
    yanzheng_ele = (By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[2]/font')
    def submit_leave_text(self,msg_title,msg_content):
        list_type_eles =self.find_elements(self.leave_type_ele)
        num = random.randint(0, len(list_type_eles)-1)
        list_type_eles[num].click()
        self.input_text(msg_title,self.msg_title_ele)
        self.input_text(msg_content,self.msg_content_ele)
        self.click_element(self.submit_btn_ele)

    def submit_leave_text_failer(self):
        text= self.get_alert_text()
        self.accept_alert()
        return text

    def submit_leave_text_success(self):
        return self.get_text(self.yanzheng_ele)