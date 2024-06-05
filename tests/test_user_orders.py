from endpoints.user_orders import UserOrders
import allure


class TestUserOrders:
    @allure.title("Проверка успешного получения заказов авторизованного пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_get_user_orders(self, token):
        user_order = UserOrders()
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        user_order.create_order(payload, token)
        response = user_order.get_user_orders(token)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка получения ошибки при получении заказов незалогином")
    @allure.description("Проверка 401 кода")
    def test_get_user_orders_without_token(self):
        user_order = UserOrders()
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        token = ''
        user_order.create_order(payload, token)
        response = user_order.get_user_orders(token)
        assert response.status_code == 401
