from behave import step

from pages.CartPage import CartPage


@step('I proceed to checkout')
def click_check_out(context):
    if "cart_page" not in context:
        context.cart_page = CartPage(context.driver)

    context.cart_page.click_check_out_button()