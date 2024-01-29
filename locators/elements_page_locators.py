from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created form

    CREATED_FULL_NAME = (By.ID, '#output #name')
    CREATED_EMAIL = (By.ID, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.ID, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.ID, '#output #permanentAddress')
