import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


@pytest.fixture()
def page(browser):
    page = MainPage(browser)
    yield page


@pytest.fixture()
def basket_page(browser):
    page = BasketPage(browser)
    yield page

    
@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, page):
        page.open()
        page.go_to_login_page()
        page.should_be_login_url()
    
    def test_guest_should_see_login_link(self, page):
        page.open()
        page.should_be_login_link()
    
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(page, basket_page):
    page.open()
    page.open_basket()
    basket_page.check_basket_is_empty()
    basket_page.should_not_be_products()
