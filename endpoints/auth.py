import requests
import urls
import allure
from endpoints.registration import Registration


class Auth(Registration):

    @allure.step('Отправляем POST запрос на авторизацию')
    def login(self, payload):
        response = requests.post(urls.BASE_URL + urls.AUTH, data=payload)
        return response

    @allure.step('Авторизация с любым payload')
    def login_with_payload(self, payload):
        return payload

