import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


@pytest.fixture()
def page(browser):
    page = ProductPage(browser)
    yield page
    
    
@pytest.fixture()
def basket_page(browser):
    page = BasketPage(browser)
    yield page
    
    
@pytest.fixture()
def login_page(browser):
    page = LoginPage(browser)
    yield page
    

@pytest.mark.parametrize(
    'number',
    [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)],
    ids=['link 1', 'link 2', 'link 3', 'link 4', 'link 5', 'link 6', 'link 7', 'link 8', 'link 9', 'link 10']
)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(page, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page.open(link=link)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_product_name()
    page.check_added_product_price()


@pytest.mark.xfail(reason="expected to fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(page):
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    

def test_guest_cant_see_success_message(page):
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="expected to fail")
def test_message_disappeared_after_adding_product_to_basket(page):
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(page):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page.open(link=link)
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(page):
    page.open()
    page.go_to_login_page()
    page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(page, basket_page):
    page.open()
    page.open_basket()
    basket_page.check_basket_is_empty()
    basket_page.should_not_be_products()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def login_user(self, login_page):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "ZZZZZZZZZZ"
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
      
    def test_user_cant_see_success_message(self, page):
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, page):
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_added_product_name()
        page.check_added_product_price()
