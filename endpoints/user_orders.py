import urls
from endpoints.orders import Orders
import requests
import allure

class UserOrders(Orders):

    @allure.step('Получить заказы любого пользователя')
    def get_user_orders(self, token):
        response = requests.get(urls.BASE_URL + urls.ORDER, headers={'Authorization': token})
        return response
