from selenium.webdriver.common.by import By

from pages.base_pages import BasePage


class MyAccountPage(BasePage):

    my_account_ele=(By.XPATH,"/html/body/div[1]/div[1]/div/div/a[1]")

    my_leave_text_ele =(By.XPATH,'/html/body/div[5]/div[1]/div/div/div/div/a[6]')


    def click_my_account(self):
        self.click_element(self.my_account_ele)

    def click_my_leave_text(self):
        self.click_element(self.my_leave_text_ele)