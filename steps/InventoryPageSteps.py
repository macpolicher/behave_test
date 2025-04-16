from behave import step

from pages.InventoryPage import InventoryPage


@step('I should be able to see the Inventory Page')
def validate_on_inventory_page(context):
    if "inventory_page" not in context:
        context.inventory_page = InventoryPage(context.driver)

    context.inventory_page.validate_url("https://www.saucedemo.com/v1/inventory.html")
    context.inventory_page.take_screenshot("SCREENSHOT_OF_INVENTORY_PAGE")

@step('I add item to cart: {item_name}')
def add_item_to_cart(context, item_name):
    if "inventory_page" not in context:
        context.inventory_page = InventoryPage(context.driver)

    context.inventory_page.add_item_to_cart(item_name)


@step('I view my cart')
def click_view_cart(context):
    if "inventory_page" not in context:
        context.inventory_page = InventoryPage(context.driver)

    context.inventory_page.view_cart()

