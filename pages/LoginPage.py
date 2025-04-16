from behave.model import Step

from pages.BasePage import BasePage
import allure

#LOCATORS
username_xpath = '//input[@id="user-name"]'
password_xpath = '//input[@id="password"]'
login_button_xpath = '//input[@id="login-button"]'

#DATA
# URL = "https://www.saucedemo.com/v1/index.html"

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    def go_to_home_page(self):
        self.open_browser(self.read_config("basic info", "URL"))


    def login(self, username, password):

        if password == 'valid_password':
            password = self.read_config('basic info', 'valid_password')

        self.enter_text(username_xpath, username)
        self.enter_text(password_xpath, password)
        self.click(login_button_xpath)

    def enter_username(self, username):
        self.enter_text(username_xpath, username)

    def enter_password(self, password):
        if password == 'valid_password':
            password = self.read_config('basic info', 'valid_password')
            self.enter_text(password_xpath, password, hide_text=True)
        else:
            self.enter_text(password_xpath, password)

    def click_login_button(self):
        self.click(login_button_xpath)
