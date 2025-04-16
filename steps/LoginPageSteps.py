import time

from behave import step

from pages.LoginPage import LoginPage

@step('I am on Sauce Demo Login Page')
def go_to_homepage(context):
    if "login_page" not in context:
        context.login_page = LoginPage(context.driver)

    context.login_page.go_to_home_page()


@step('I enter username: {username}, password: {password}')
def login_to_page(context, username, password):
    if "login_page" not in context:
        context.login_page = LoginPage(context.driver)

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login_button()
    # context.login_page.accept_alert_if_present()
    time.sleep(10)
