from behave import step

from pages.FinishPage import FinishPage


@step('I should be able to see the Pony Express Icon')
def validate_pony_express_icon(context):
    if "finish_page" not in context:
        context.finish_page = FinishPage(context.driver)

    context.finish_page.validate_pony_express_image_present()