from endpoints.registration import Registration
import allure


class TestRegistration:

    @allure.title("Проверка успешной регистрации пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_registration_userк(self, registration):
        new_user = Registration()
        response = new_user.registration_user(registration)
        assert response.status_code == 200 and response.json()['success'] == True


    @allure.title("Проверка регистрации одного и того же пользователя")
    @allure.description("Проверка 403 кода и ответа 'User already exists'")
    def test_create_the_same_user(self, registration_the_same_user):
        new_user = Registration()
        response = new_user.registration_user(registration_the_same_user)
        assert response.status_code == 403 and response.json()['message'] == 'User already exists'


    @allure.title("Проверка регистрации пользователя с одним пустым полем")
    @allure.description("Проверка 403 кода и ответа 'Email, password and name are required fields'")
    def test_create_user_with_empty_field(self):
        new_user = Registration()
        response = new_user.create_user_with_empty_field()
        assert response.status_code == 403 and response.json()['message'] == 'Email, password and name are required fields'