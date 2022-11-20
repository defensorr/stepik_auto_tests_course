from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def check_added_product_name(self):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERTS)
        product_description = alerts[0].text
        name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        text = f'{name} has been added to your basket.'
        self.verify_label_text(text=text, actual=product_description)
        
    def check_added_product_price(self):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERTS)
        product_description = alerts[2].text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        text = f'Your basket total is now {price}\nView basket Checkout now'
        self.verify_label_text(text=text, actual=product_description)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def dissapered_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"