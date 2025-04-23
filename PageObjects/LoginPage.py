import time

from selenium.webdriver.common.by import By

from Utils.BrowserUtils import BrowserUtils


class LoginPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.text_username_id = (By.ID,"user-name")
        self.text_password_id = (By.ID,"password")
        self.button_submit_id = (By.ID,"login-button")
        self.title_page_css = (By.CSS_SELECTOR,".title")


    def loginPageFn(self, username, password):
        self.driver.find_element(*self.text_username_id).send_keys(username)
        self.driver.find_element(*self.text_password_id).send_keys(password)
        self.driver.find_element(*self.button_submit_id).click()
        return self.driver.find_element(*self.title_page_css).text

    def goto_url(self, url):
        self.driver.get(url)

    def loginPageFn1(self, username, password):
        self.driver.find_element(*self.text_username_id).send_keys(username)
        self.driver.find_element(*self.text_password_id).send_keys(password)
        self.driver.find_element(*self.button_submit_id).click()
