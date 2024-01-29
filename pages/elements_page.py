import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys(self, 'me')
        self.element_is_visible(self.locators.EMAIL).send_keys(self, 'me@gm.ccom')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(self, 'street')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(self, 'street, city, state')
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)
