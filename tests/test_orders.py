from endpoints.orders import Orders
import allure


class TestOrders:
    @allure.title("Проверка успешного создания заказа авторизованным пользователем")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_create_order(self, token):
        order = Orders()
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        response = order.create_order(payload, token)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа незалогином")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_create_order_without_auth(self):
        order = Orders()
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        token = ''
        response = order.create_order(payload, token)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа без ингридиентов незалогином")
    @allure.description("Проверка 400 кода и ответа 'success' == True")
    def test_create_order_no_ingridient_no_token(self):
        order = Orders()
        payload = {"ingredients": []}
        token = ''
        response = order.create_order(payload, token)
        assert response.status_code == 400 and response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title("Проверка создания заказа без ингридиентов зарегистрированным пользователем")
    @allure.description("Проверка 400 кода и ответа 'Internal Server Error' == True")
    def test_create_order_no_ingridient(self, token):
        order = Orders()
        payload = {"ingredients": []}
        response = order.create_order(payload, token)
        assert response.status_code == 400 and response.json()['message'] == 'Ingredient ids must be provided'


    @allure.title("Проверка создания заказа с невалидным хэш ингридиента")
    @allure.description("Проверка 500 кода и ответа 'Internal Server Error'")
    def test_create_order_invalid_hash(self):
        order = Orders()
        payload = {"ingredients": ["61c0c5a7182001bfaaa6d", "61c0c5a71ddf82001bdaaa6f"]}
        token = ''
        response = order.create_order(payload, token)
        assert response.status_code == 500 and 'Internal Server Error' in response.text

