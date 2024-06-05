import requests
import urls
from random import randint
import allure
from faker import Faker

class Registration:

    @allure.step('Создаем payload')
    def create_payload(self):
        fake = Faker()
        username = fake.first_name()
        email = fake.email()
        password = fake.password(randint(6, 10))

        payload = {
            "email": email,
            "password": password,
            "name": username
        }

        return payload


    @allure.step('Создаем нового пользователя любым payload, возвращаем POST запрос')
    def create_user(self, payload):
        return requests.post(urls.BASE_URL + urls.REGISTRATION, data=payload)

    @allure.step('Удаляем пользователя')
    def delete_user(self, payload, token):
        requests.delete(urls.BASE_URL + urls.DELETE_UPDATE, data=payload, headers={'Authorization': token})

    @allure.step('Регистрация любого пользователя')
    def registration_user(self, payload):
        return payload


    @allure.step('Регистрация пользователя с пустым полем')
    def create_user_with_empty_field(self):
        payload = self.create_payload()
        payload['name'] = ''
        response = self.create_user(payload)
        return response








