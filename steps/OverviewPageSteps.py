from behave import step

from pages.OverviewPage import OverviewPage


@step('I click on finish button')
def click_finish_button(context):
    if "overview_page" not in context:
        context.overview_page = OverviewPage(context.driver)

    context.overview_page.click_finish_button()