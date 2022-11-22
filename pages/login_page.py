from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    
    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.EMAIL_FIELD
        ).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD_FIELD
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_BTN
        ).click()
    