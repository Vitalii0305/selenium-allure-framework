from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def log(self, message):
        print(f"[STEP] {message}")

    @allure.step("Відкриваємо сторінку: {url}")
    def open_url(self, url):
        self.log(f"Opening {url}")
        self.driver.get(url)

    @allure.step("Клікаю на елемент {locator}")
    def click(self, locator):
        self.log(f"Clicking {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Заповнюю поле {locator} текстом '{text}'")
    def fill(self, locator, text):
        self.log(f"Filling {locator} with {text}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Отримую текст з елемента {locator}")
    def get_text(self, locator):
        self.log(f"Getting text from {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Очікую появу елемента {locator}")
    def wait_for_element(self, locator, timeout=10):
        self.log(f"Waiting for element {locator}")
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
