from selenium.webdriver.common.by import By

from pages.base_pages import BasePage


class LoginPage(BasePage):
    username_ele = (By.NAME, 'username')
    password_ele = (By.NAME, 'password')
    checkbox_ele = (By.ID, 'remember')
    login_button_ele = (By.NAME, 'submit')
    password_question_ele = (By.LINK_TEXT, '密码问题找回密码')
    email_question_ele = (By.LINK_TEXT, '注册邮件找回密码')
    login_url = "http://192.168.190.132/ecshop/user.php"

    text_ele = (By.XPATH,'//*[@id="ECS_MEMBERZONE"]/a[1]')

    def login(self, username, password):

        self.input_text(username, self.username_ele)
        self.input_text(password, self.password_ele)
        self.click_element(self.checkbox_ele)
        self.click_element(self.login_button_ele)


    def login_success(self):
        return self.get_text(self.text_ele)


    def login_failer(self):
        text = self.get_alert_text()
        self.accept_alert()
        return text


