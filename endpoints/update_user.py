import requests
import urls
import allure
from endpoints.auth import Auth


class Update(Auth):

    @allure.step('Отправляем запрос на обновление, возвращаем Patch')
    def update(self, payload, token):
        response = requests.patch(urls.BASE_URL + urls.DELETE_UPDATE, data=payload, headers={'Authorization': token})
        return response

    @allure.step('Отправляем запрос на обновление')
    def update_user(self, payload):
        return payload

    @allure.step('Отправляем запрос на обновление без авторизации')
    def update_user_without_auth(self):
        payload = self.create_payload()
        token = ''
        response = self.update(payload, token)
        return response



