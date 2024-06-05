from endpoints.auth import Auth
import allure

class TestAuth:
    @allure.title("Проверка успешной авторизации пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_login_with_payload(self, auth):
        user = Auth()
        response = user.login_with_payload(auth)
        assert response.status_code == 200 and response.json()['success'] == True


    @allure.title("Проверка авторизации c неверным паролем пользователя")
    @allure.description("Проверка 401 кода и ответа 'message' == 'email or password are incorrect'")
    def test_login_incorrect_payload(self, auth_incorrect):
        user = Auth()
        response = user.login_with_payload(auth_incorrect)
        assert response.status_code == 401 and response.json()['message'] == 'email or password are incorrect'
