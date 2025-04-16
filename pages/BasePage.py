from configparser import ConfigParser

import selenium.webdriver
from behave.model import Step

from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

TIME_OUT = 30

class BasePage:
    def __init__(self, driver):
        self.driver = driver

        # FOR DEBUG AND SETTING UP
        # self.driver = selenium.webdriver.Chrome(service=Service(executable_path='drivers/chromedriver.exe'))




    def open_browser(self, url):
        self.driver.get(url)


    def find_element(self, locator):
        try:
            return WebDriverWait(self.driver, TIME_OUT).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="ELEMENT_NOT_FOUND", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"element not found with locator: ***{locator}*** \n \n {ex}")

    def enter_text(self, locator, keys_to_send, hide_text=False):
        # LET'S HIDE TEXT IF hide_text = True
        text = ""
        if hide_text:
            text = "**********"
        else:
            text = keys_to_send

        with allure.step(f"send keys: {text}"):
            self.find_element(locator).send_keys(keys_to_send)

    def click(self, locator):
        self.find_element(locator).click()

    def validate_url(self, url):
        try:
            with allure.step(f"validating expected url: {url}"):
                WebDriverWait(self.driver, TIME_OUT).until(EC.url_to_be(url))
        except Exception:
            # print(f"WRONG URL! EXPECTED: [{url}] is not the same as actual." + "\n" + str(ex))
            self.take_screenshot("WRONG_URL!")
            raise Exception(f"WRONG URL! EXPECTED: [{url}] is not the same as ACTUAL: [{self.driver.current_url}]")



    @staticmethod
    def read_config(category, key):
        config = ConfigParser()
        config.read('configurations/config.ini')

        return config.get(category, key)

    def take_screenshot(self, name_of_screenshot):
        allure.attach(self.driver.get_screenshot_as_png(), name=name_of_screenshot,
                      attachment_type=allure.attachment_type.PNG)

    def accept_alert_if_present(self):
        try:
            # Wait for the alert to be present
            # WebDriverWait(driver, 10).until(EC.alert_is_present())
            WebDriverWait(self.driver, TIME_OUT).until(EC.alert_is_present())

            # Switch to the alert
            alert = self.driver.switch_to.alert

            # Print the alert text
            print("Alert detected: ", alert.text)

            # Accept the alert
            alert.accept()
        except TimeoutException:
            print("No alert detected within timeout.")