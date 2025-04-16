from pages.BasePage import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def validate_on_inventory_page_url(self, url):
        self.validate_url(url)