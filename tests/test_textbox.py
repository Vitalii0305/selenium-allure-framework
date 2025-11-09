import json
import pytest
import allure

@allure.feature("Заповнення форми")
@allure.story("Перевірка валідного та невалідного заповнення")
def load_test_data():
    with open("test_textbox_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data())
@allure.title("Перевірка заповнення форми Text Box")
@allure.severity(allure.severity_level.CRITICAL)
def test_textbox_form(open_page, data):
    name = data["name"]
    email = data["email"]
    current = data["current"]
    permanent = data["permanent"]
    should_fail = data["should_fail"]

    page = open_page
    page.fill_form(name, email, current, permanent)
    field = page.get_email_field()

    if should_fail:
        assert "field-error" in field.get_attribute("class")
    else:
        result = page.get_result_text()
        assert name in result
        assert email in result
        assert current in result
        assert permanent in result
