from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class TextBoxPage(BasePage):
    EMAIL_FIELD = (By.ID, "userEmail")

    def open(self):
        self.open_url("https://demoqa.com/text-box")

    @allure.step("Заповнюємо форму даними: {name}, {email}")
    def fill_form(self, name, email, current, permanent):
        self.fill((By.ID, "userName"), name)
        self.fill((By.ID, "userEmail"), email)
        self.fill((By.ID, "currentAddress"), current)
        self.fill((By.ID, "permanentAddress"), permanent)
        self.click((By.ID, "submit"))

    @allure.step("Отримуємо текст результату")
    def get_result_text(self):
        return self.get_text((By.ID, "output"))

    @allure.step("Отримуємо поле email")
    def get_email_field(self):
        return self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD))
