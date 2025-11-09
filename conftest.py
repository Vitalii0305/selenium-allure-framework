import pytest
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.check_box_page import CheckboxPage
from pages.text_box_page import TextBoxPage

@pytest.fixture
def driver():
    print("\n[SETUP] Відкриваємо браузер...")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    print("\n[TEARDOWN] Закриваємо браузер...")
    driver.quit()

@pytest.fixture
def open_page(request, driver):
    """Визначає, яку сторінку потрібно відкрити залежно від тесту"""
    test_name = request.node.name.lower()

    if "checkbox" in test_name:
        page = CheckboxPage(driver)
    elif "textbox" in test_name:
        page = TextBoxPage(driver)
    else:
        pytest.skip(reason="Невідома сторінка для цього тесту")

    page.open()
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            allure.attach.file(
                screenshot_path,
                name=f"Screenshot: {item.name}",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                driver.current_url,
                name="Current URL",
                attachment_type=allure.attachment_type.TEXT
            )
