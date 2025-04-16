from pages.BasePage import BasePage


# LOCATORS
finish_button_xpath = '//a[@href="./checkout-complete.html"]'

class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_finish_button(self):
        self.click(finish_button_xpath)