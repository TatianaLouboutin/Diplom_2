import data
from endpoints.user_orders import UserOrders
import allure


class TestUserOrders:
    @allure.title("Проверка успешного получения заказов авторизованного пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_get_user_orders(self, auth_token):
        user_order = UserOrders()
        payload = data.VALID_INGRIDIENTS
        user_order.create_order(payload, auth_token[0])
        response = user_order.get_user_orders(auth_token[0])
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка получения ошибки при получении заказов незалогином")
    @allure.description("Проверка 401 кода")
    def test_get_user_orders_without_token(self):
        user_order = UserOrders()
        payload = data.VALID_INGRIDIENTS
        token = ''
        user_order.create_order(payload, token)
        response = user_order.get_user_orders(token)
        assert response.status_code == 401
