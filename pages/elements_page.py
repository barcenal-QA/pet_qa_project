from locators.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_all_fields