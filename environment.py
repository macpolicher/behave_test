from allure_commons.model2 import Attachment
from behave import fixture, use_fixture
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
import allure

@fixture
def setup_chrome_driver(context):
    context.driver = selenium.webdriver.Chrome(service=Service('drivers/chromedriver.exe'))
    context.driver.maximize_window()
    # allure.attach(context.driver.get_screenshot_as_png(), name="screenshot_failed", attachment_type=Attachment)
    yield context.driver

    context.driver.quit()


def before_all(context):
    use_fixture(setup_chrome_driver, context)


# def after_step(context, step):
#     if step.status == 'failed':
#         allure.attach(context.driver.)