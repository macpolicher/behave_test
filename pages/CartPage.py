from pages.BasePage import BasePage

#LOCATORS
checkout_button = '//a[@href="./checkout-step-one.html"]'

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def click_check_out_button(self):
        self.click(checkout_button)
