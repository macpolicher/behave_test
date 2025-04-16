from pages.BasePage import BasePage


#LOCATORS
f_name_xpath = '//input[@id="first-name"]'
l_name_xpath = '//input[@id="last-name"]'
zip_code_xpath = '//input[@id="postal-code"]'
continue_button_xpath = '//input[@type="submit" and @value="CONTINUE"]'

class YourInformationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def enter_first_name(self, f_name):
        self.enter_text(f_name_xpath, f_name)

    def enter_last_name(self, l_name):
        self.enter_text(l_name_xpath, l_name)

    def enter_zip_code(self, zip_code):
        self.enter_text(zip_code_xpath, zip_code)

    def click_continue_button(self):
        self.click(continue_button_xpath)