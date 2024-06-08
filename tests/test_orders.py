from endpoints.orders import Orders
import allure
import data

class TestOrders:
    @allure.title("Проверка успешного создания заказа авторизованным пользователем")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_create_order(self, auth_token):
        order = Orders()
        payload = data.VALID_INGRIDIENTS
        response = order.create_order(payload, auth_token[0])
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа незалогином")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_create_order_without_auth(self):
        order = Orders()
        payload = data.VALID_INGRIDIENTS
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
        assert response.status_code == 400 and response.json()['message'] == data.MESSAGE_NO_ONGRIDIENT

    @allure.title("Проверка создания заказа без ингридиентов зарегистрированным пользователем")
    @allure.description("Проверка 400 кода и ответа 'Internal Server Error' == True")
    def test_create_order_no_ingridient(self, auth_token):
        order = Orders()
        payload = {"ingredients": []}
        response = order.create_order(payload, auth_token[0])
        assert response.status_code == 400 and response.json()['message'] == data.MESSAGE_NO_ONGRIDIENT


    @allure.title("Проверка создания заказа с невалидным хэш ингридиента")
    @allure.description("Проверка 500 кода и ответа 'Internal Server Error'")
    def test_create_order_invalid_hash(self):
        order = Orders()
        payload = data.INVALID_HASH
        token = ''
        response = order.create_order(payload, token)
        assert response.status_code == 500 and 'Internal Server Error' in response.text

