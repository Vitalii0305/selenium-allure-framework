from conftest import open_page
from pages.check_box_page import CheckboxPage
import allure

@allure.feature("Чекбокс")
@allure.story("Перевірка роботи чекбоксу та тексту")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Перевірка чекбоксу 'Home'")
def test_checkbox_home(open_page):
    page = open_page
    page.expand_all()
    page.select_checkbox()
    result = page.get_home_text()
    assert "home" in result.lower()
