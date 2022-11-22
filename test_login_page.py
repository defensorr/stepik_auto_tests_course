import pytest
from .pages.login_page import LoginPage


@pytest.fixture()
def page(browser):
    page = LoginPage(browser)
    yield page
    
    
def test_login_page_url(page):
    page.open()
    page.should_be_login_url()
   
    
def test_login_page_login_form(page):
    page.open()
    page.should_be_login_form()
    
    
def test_login_page_register_form(page):
    page.open()
    page.should_be_register_form()
