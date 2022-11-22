from selenium.common.exceptions import (
	NoSuchElementException,
	NoAlertPresentException,
	TimeoutException
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
import math


class BasePage:
	def __init__(self, browser, timeout=3):
		self.browser = browser
		self.browser.implicitly_wait(timeout)
	
	url = None
		
	def check_page_url(self, url):
		current_url = self.browser.current_url
		assert current_url == url, f"Current url:{url} is not as expected url:{current_url}"
		
	def go_to_login_page(self):
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()
	
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		
		return True
	
	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(
				EC.presence_of_element_located((how, what))
			)
		except TimeoutException:
			return True
		
		return False
	
	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, [TimeoutException]).until_not(
				EC.presence_of_element_located((how, what))
			)
		except TimeoutException:
			return False
		
		return True
	
	def open(self, link=None):
		self.browser.get(link or self.url)
		
	def open_basket(self):
		self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()
	
	def should_be_login_link(self):
		assert self.is_element_present(
			*BasePageLocators.LOGIN_LINK), "Login link is not presented"
	
	def should_be_login_url(self):
		self.check_page_url(
			'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
		)
	
	def should_be_authorized_user(self):
		assert self.is_element_present(
			*BasePageLocators.USER_ICON
		), "User icon is not presented, probably unauthorised user"
		
	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
			
	def verify_label_text(self, text, how, what):
		actual = self.browser.find_element(how, what).text
		assert actual == text, (
			f'Unexpected label text.\nExpected: {text}\nGot: {actual}'
		)
