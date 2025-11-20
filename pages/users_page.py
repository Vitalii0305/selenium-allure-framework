from pages.base_page import BasePage
from  selenium.common.exceptions import *
from selenium.webdriver.common.by import By
import allure

class UsersPage(BasePage):
    USER_NAME = (By.XPATH , "//div[contains(@class, 'user-name') and text()='{name}']")

    @allure.step("Open user page")
    def open_user_page(self):
        self.open_url("https://demoqa.com/users")

    @allure.step("Checking user is present")
    def is_user_present(self, name):
        locator = (self.USER_NAME[0], self.USER_NAME[1].format(name=name))
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
