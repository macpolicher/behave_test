from pages.BasePage import BasePage


# LOCATORS
pony_img_xpath = '//img[@src="img/pony-express.png"]'

class FinishPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def validate_pony_express_image_present(self):
        self.find_element(pony_img_xpath)