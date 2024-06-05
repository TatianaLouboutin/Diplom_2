from endpoints.update_user import Update
import allure

class TestUpdateUser:
    @allure.title("Проверка успешной обновления данных пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_(self, update_user):
        user = Update()
        response = user.update_user(update_user)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка обновления для неавторизованного пользователя")
    @allure.description("Проверка 401 кода и ответа 'message' == 'You should be authorised'")
    def test_update_user_without_auth(self):
        user = Update()
        response = user.update_user_without_auth()
        assert response.status_code == 401 and response.json()['message'] == 'You should be authorised'