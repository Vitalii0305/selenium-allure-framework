import allure
from allure_commons.types import AttachmentType

from api.user_api import UsersAPI
from pages.users_page import UsersPage

BASE_URL = "https://reqres.in/api"

@allure.feature("User Creation")
@allure.story("User creation with api and audition by UI")
def test_user_creation(driver):
    name="Vitalii"
    job="QA Engineer"

    api = UsersAPI(BASE_URL)
    with allure.step("Create new user"):
        response = api.create_user(name, job)
        assert(response.status_code == 201)
        user_data = response.json()
        allure.attach(str(user_data), name="User creation with api and audition by UI",attachment_type=AttachmentType.JSON)

    page = UsersPage(driver)
    page.open()

    with allure.step("Check if user exists"):
        assert page.is_user_present(name) , f"User {name} doesn't exist"