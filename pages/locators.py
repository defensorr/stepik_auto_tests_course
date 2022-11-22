from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class*=basket] a[class*=btn-default]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "[id='messages'] div div")
    PRODUCT_ADDED_PRICE = (By.CSS_SELECTOR, "[class*=alert-info] p")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[class*='product_main'] h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p[class*='price_color']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id='messages'] div div")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CLASS_NAME, "content")
    PRODUCTS_LIST = (By.CLASS_NAME, "basket-items")
