from selenium.webdriver.common.by import By


class TextBoxLocators:

    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:

    EXPAND_BUTTON = (By.CSS_SELECTOR, ".rc-tree-switcher.rc-tree-switcher_close")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rc-tree-checkbox']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "[aria-checked='true']")
    TITLE_ITEM = (By.XPATH, "./following-sibling::span")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")



