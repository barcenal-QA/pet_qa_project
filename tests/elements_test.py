import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
from utils.normalization import normalize

class TestElements:

    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            assert full_name == output_name, 'full_name doesn`t match'
            assert email == output_email, 'email doesn`t match'
            assert current_address == output_cur_addr, 'current address doesn`t match'
            assert permanent_address == output_per_addr, 'permanenet adress doesn`t match'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()

            assert normalize(input_checkbox) == normalize(output_result)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            try:
                radio_button_page.click_on_radio_button('no')
                output_no = radio_button_page.get_output_result()

            except Exception:
                print("Radio button 'No' isn't clickable")

            assert output_yes == 'Yes', "radio button 'Yes' isn`t selected"
            assert output_impressive == 'Impressive', "radio button 'Impressive' isn`t selected"
