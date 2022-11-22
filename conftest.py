import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser language: ru or en or es")
    
    
@pytest.fixture(scope="function", autouse=True)
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    browser = Chrome(chrome_options=options)
    browser.set_window_size(1420, 800)
    yield browser
    browser.quit()
