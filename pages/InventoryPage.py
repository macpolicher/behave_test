from pages.BasePage import BasePage

#LOCATORS
cart_icon_xpath = '//a[@href="./cart.html"]'




class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def validate_on_inventory_page_url(self, url):
        self.validate_url(url)

    def add_item_to_cart(self, name_of_item):
        self.click(f'//div[@class="inventory_item_name"][text()="{name_of_item}"]/ancestor::div[@class="inventory_item"]//button[text()="ADD TO CART"]')

    def view_cart(self):
        self.click(cart_icon_xpath)
