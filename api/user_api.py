import allure
from api.base_api import BaseAPI

class UsersAPI(BaseAPI):
    @allure.step("Створюємо користувача через API")
    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        response = self.request("POST", "/users", json=payload)
        return response