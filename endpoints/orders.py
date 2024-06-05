import urls
from endpoints.auth import Auth
import requests
import allure

class Orders(Auth):

    @allure.step('Создание заказа любым payload')
    def create_order(self, payload, token):
        response = requests.post(urls.BASE_URL + urls.ORDER, data=payload, headers={'Authorization': token})
        return response

