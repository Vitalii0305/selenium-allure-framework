from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class CheckboxPage(BasePage):
    EXPAND_ALL = (By.XPATH, "//button[@aria-label='Expand all']")
    HOME_CHECKBOX = (By.XPATH, "(//span[@class='rct-checkbox'])[1]")
    TEXT_AREA = (By.XPATH, "//span[text()='home']")

    @allure.step("Відкриваємо сторінку Checkbox")
    def open(self):
        self.open_url("https://demoqa.com/checkbox")

    @allure.step("Розгортаємо всі чекбокси")
    def expand_all(self):
        element = self.wait.until(EC.element_to_be_clickable(self.EXPAND_ALL))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Обираємо чекбокс 'Home'")
    def select_checkbox(self):
        self.click(self.HOME_CHECKBOX)

    @allure.step("Отримуємо текст результату")
    def get_home_text(self):
        return self.get_text(self.TEXT_AREA)
