from selenium.webdriver.common.by import By


class TextBoxLocators:

    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "input[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "input[id='permanentAddress']")
    SUBMIT = By.CSS_SELECTOR, "input[id='submit']"

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "output[id='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "output[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "output[id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "output[id='permanentAddress']")