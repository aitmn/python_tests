import time

from pages.elements_page import TextBoxPage
from conftest import driver


class TestElementsPage:
    class TestTextBoxPage:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(5)
