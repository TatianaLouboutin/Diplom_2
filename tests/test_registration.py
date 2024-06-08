import data
from endpoints.registration import Registration
import allure


class TestRegistration:

    @allure.title("Проверка успешной регистрации пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_registration_user(self, payload):
        assert payload[1].status_code == 200 and payload[1].json()['success'] == True


    @allure.title("Проверка регистрации одного и того же пользователя")
    @allure.description("Проверка 403 кода и ответа 'User already exists'")
    def test_create_the_same_user(self, payload):
        new_user = Registration()
        response = new_user.create_user(payload[0])
        assert response.status_code == 403 and response.json()['message'] == data.MESSAGE_USER_EXIST


    @allure.title("Проверка регистрации пользователя с одним пустым полем")
    @allure.description("Проверка 403 кода и ответа 'Email, password and name are required fields'")
    def test_create_user_with_empty_field(self):
        new_user = Registration()
        response = new_user.create_user_with_empty_field()
        assert response.status_code == 403 and response.json()['message'] == data.MESSAGE_EMPTY_FIELD