from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    url = "http://selenium1py.pythonanywhere.com/en-gb/basket/"

    def check_basket_is_empty(self):
        text = 'Your basket is empty. Continue shopping'
        self.verify_label_text(text, *BasketPageLocators.EMPTY_BASKET_MESSAGE)
        
    def should_not_be_products(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_LIST
        ), "Product is presented, but should not be"
