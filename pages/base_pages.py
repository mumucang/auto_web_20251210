import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

import config
from utils.logger_util import LoggerUtil


class BasePage:
    def __init__(self, driver=None):
        """
        初始化BasePage类
        :param driver: WebDriver实例
        """
        if driver is None:
            op = webdriver.EdgeOptions()
            op.add_argument("--no-sandbox")
            op.add_argument("--disable-dev-shm-usage")
            op.add_argument("--disable-gpu")
            op.add_argument("--headless")
            service = Service(executable_path=r"D:\software\Python314\msedgedriver.exe")
            self.driver = webdriver.Edge(options=op,service=service)
        else:
            self.driver = driver

        self.base_url = config.project_url  # 设置基础URL
        self.timeout = 30  # 设置默认等待时间

        self.logger = LoggerUtil.get_logger(name='my_web_logger', level=logging.DEBUG, file_name='web')

    def open_page(self, url=None):
        """
        打开指定URL，如果没有传入URL，则打开基础URL
        :param url: 要打开的URL
        """
        url = url if url else self.base_url
        self.driver.get(url)
        self.driver.maximize_window()
        self.logger.info(f"Opened page: {url}")

    def find_element(self, locator):
        """
        查找单个元素
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回找到的元素
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element found: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found within {self.timeout} seconds: {locator}")
            return None
        except NoSuchElementException:
            self.logger.error(f"Element not found: {locator}")
            return None

    def find_elements(self, locator):
        """
        查找多个元素
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回找到的元素列表
        """
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
            self.logger.info(f"Elements found: {locator}")
            return elements
        except TimeoutException:
            self.logger.error(f"Elements not found within {self.timeout} seconds: {locator}")
            return []
        except NoSuchElementException:
            self.logger.error(f"Elements not found: {locator}")
            return []

    def click_element(self, locator):
        """
        点击元素
        :param locator: 传入定位器，如(By.ID, "example")
        """
        element = self.find_element(locator)
        if element:
            element.click()
            self.logger.info(f"Clicked element: {locator}")

    def input_text(self, text, locator):
        """
        向元素输入文本
        :param text: 输入的文本
        :param locator: 传入定位器，如(By.ID, "example")
        """
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Input text: '{text}' into element: {locator}")

    def get_text(self, locator):
        """
        获取元素文本
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回元素的文本内容
        """
        element = self.find_element(locator)
        if element:
            text = element.text
            self.logger.info(f"Got text: '{text}' from element: {locator}")
            return text
        return ""

    def is_element_visible(self, locator):
        """
        判断元素是否可见
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回布尔值，表示元素是否可见
        """
        try:
            visible = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element is visible: {locator}")
            return visible
        except TimeoutException:
            self.logger.error(f"Element not visible within {self.timeout} seconds: {locator}")
            return False
        except NoSuchElementException:
            self.logger.error(f"Element not found: {locator}")
            return False

    def wait_until_element_clickable(self, locator):
        """
        等待元素可点击
        :param locator: 传入定位器，如(By.ID, "example")
        :return: 返回可点击的元素
        """
        try:
            clickable = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
            self.logger.info(f"Element is clickable: {locator}")
            return clickable
        except TimeoutException:
            self.logger.error(f"Element not clickable within {self.timeout} seconds: {locator}")
            return None
        except NoSuchElementException:
            self.logger.error(f"Element not found: {locator}")
            return None

    def scroll_to_element(self, locator):
        """
        滚动到指定元素
        :param locator: 传入定位器，如(By.ID, "example")
        """
        element = self.find_element(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.logger.info(f"Scrolled to element: {locator}")

    def refresh_page(self):
        """
        刷新当前页面
        """
        self.driver.refresh()
        self.logger.info("Page refreshed")

    def back_to_previous_page(self):
        """
        返回上一页
        """
        self.driver.back()
        self.logger.info("Navigated back to previous page")

    def forward_to_next_page(self):
        """
        前进到下一页
        """
        self.driver.forward()
        self.logger.info("Navigated forward to next page")

    def execute_script(self, script):
        """
        执行JavaScript脚本
        :param script: JavaScript脚本字符串
        """
        self.driver.execute_script(script)
        self.logger.info(f"Executed JavaScript script: {script}")

    def switch_to_frame(self, locator):
        """
        切换到iframe
        :param locator: 传入定位器，如(By.ID, "example")
        """
        frame = self.find_element(locator)
        if frame:
            self.driver.switch_to.frame(frame)
            self.logger.info(f"Switched to frame: {locator}")

    def switch_to_default_content(self):
        """
        切换回默认内容
        """
        self.driver.switch_to.default_content()
        self.logger.info("Switched to default content")

    def switch_to_window(self, window_handle):
        """
        切换到指定的窗口句柄
        :param window_handle: 窗口句柄
        """
        self.driver.switch_to.window(window_handle)
        self.logger.info(f"Switched to window with handle: {window_handle}")

    def get_current_window_handle(self):
        """
        获取当前窗口句柄
        :return: 当前窗口句柄
        """
        current_handle = self.driver.current_window_handle
        self.logger.info(f"Current window handle: {current_handle}")
        return current_handle

    def get_all_window_handles(self):
        """
        获取所有窗口句柄
        :return: 所有窗口句柄的列表
        """
        all_handles = self.driver.window_handles
        self.logger.info(f"All window handles: {all_handles}")
        return all_handles

    def take_screenshot(self, filename):
        """
        截取当前页面截图
        :param filename: 截图保存的文件名
        """
        str_time = time.strftime("%Y%m%d%H%M%S")
        path = os.path.join(config.pictures_path, f"{filename}{str_time}.png")
        self.driver.save_screenshot(path)
        self.logger.info(f"Screenshot saved as: {path}")

    def get_page_title(self):
        """
        获取当前页面的标题
        :return: 页面标题
        """
        title = self.driver.title
        self.logger.info(f"Page title: {title}")
        return title

    def get_page_url(self):
        """
        获取当前页面的URL
        :return: 页面URL
        """
        url = self.driver.current_url
        self.logger.info(f"Page URL: {url}")
        return url

    def wait_for_page_load(self, timeout=30):
        """
        等待页面加载完成
        :param timeout: 等待时间，默认30秒
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            self.logger.info("Page loaded successfully")
        except TimeoutException:
            self.logger.error(f"Page did not load within {timeout} seconds")

    def close_page(self):
        self.driver.quit()


    def accept_alert(self):
        """
        接受警告框
        """
        alert = self.driver.switch_to.alert
        alert.accept()
        self.logger.info("Alert accepted")

    def dismiss_alert(self):
        """
        取消警告框
        """
        alert = self.driver.switch_to.alert
        alert.dismiss()
        self.logger.info("Alert dismissed")

    def get_alert_text(self):
        """
        获取警告框文本
        :return: 警告框文本
        """
        alert = self.driver.switch_to.alert
        text = alert.text
        self.logger.info(f"Alert text: {text}")
        return text

    def send_keys_to_alert(self, keys):
        """
        向警告框输入文本
        :param keys: 要输入的文本
        """
        alert = self.driver.switch_to.alert
        alert.send_keys(keys)
        self.logger.info(f"Sent keys to alert: {keys}")




