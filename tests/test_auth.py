from endpoints.auth import Auth
import data
import allure

class TestAuth:
    @allure.title("Проверка успешной авторизации пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_login_with_payload(self, auth_token):
        assert auth_token[1].status_code == 200 and auth_token[1].json()['success'] == True


    @allure.title("Проверка авторизации c неверным паролем пользователя")
    @allure.description("Проверка 401 кода и ответа 'message' == 'email or password are incorrect'")
    def test_login_incorrect_payload(self, auth_token):
        auth = Auth()
        auth_token[2]['password'] = 'wwww1222'
        response = auth.login(auth_token[2])
        assert response.status_code == 401 and response.json()['message'] == data.MESSAGE_EMAIL_INCORRECT
