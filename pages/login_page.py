from pages.base_page import BasePage
from pages.locators import LoginPageLocators, RegisterPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self, url):
        current_url = self.browser.current_url
        assert current_url == url, f"Current url:{url} is not as expected url:{current_url}"
        assert True

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert True

    def should_be_register_form(self):
        self.is_element_present(*RegisterPageLocators.REGISTER_FORM)
        assert True
