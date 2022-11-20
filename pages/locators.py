from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    

class RegisterPageLocators:
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")
    ALERTS = (By.CSS_SELECTOR, "[id='messages'] div div")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[class*='product_main'] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p[class*='price_color']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id='messages'] div div")
    