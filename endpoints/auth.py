import requests
import urls
import allure
from endpoints.registration import Registration


class Auth(Registration):

    @allure.step('Отправляем POST запрос на авторизацию')
    def login(self, payload):
        response = requests.post(urls.BASE_URL + urls.AUTH, data=payload)
        return response



