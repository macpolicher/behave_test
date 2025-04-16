from behave import step

from pages.YourInformationPage import YourInformationPage


@step('I enter my details and continue, first name: {f_name}, last name: {l_name}, zip_code: {zip_code}')
def enter_my_info(context, f_name, l_name, zip_code):
    if "info_page" not in context:
        context.info_page = YourInformationPage(context.driver)

    context.info_page.enter_first_name(f_name)
    context.info_page.enter_last_name(l_name)
    context.info_page.enter_zip_code(zip_code)
    context.info_page.click_continue_button()
