from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def check_added_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        text = f'{name} has been added to your basket.'
        self.verify_label_text(text, *ProductPageLocators.PRODUCT_ADDED_MESSAGE)
        
    def check_added_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        text = f'Your basket total is now {price}'
        self.verify_label_text(text, *ProductPageLocators.PRODUCT_ADDED_PRICE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"
