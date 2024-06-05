import pytest
from endpoints.registration import Registration
from endpoints.auth import Auth
from endpoints.update_user import Update
from endpoints.orders import Orders
import allure



@allure.step("Регистрация нового пользователя и удаление его по окончании теста")
@pytest.fixture(scope='function')
def registration():
    new_user = Registration()
    payload = new_user.create_payload()
    response = new_user.create_user(payload)
    yield response
    token = response.json()['accessToken']
    new_user.delete_user(payload, token)



@allure.step("Регистрация нового пользователя второй раз и удаление его по окончании теста")
@pytest.fixture(scope='function')
def registration_the_same_user():
    new_user = Registration()
    payload = new_user.create_payload()
    response = new_user.create_user(payload)
    response_second = new_user.create_user(payload)
    yield response_second
    token = response.json()['accessToken']
    new_user.delete_user(payload, token)


@allure.step("Авторизация пользователя и удаление его по окончании теста")
@pytest.fixture(scope='function')
def auth():
    new_user = Auth()
    payload = new_user.create_payload()
    new_user.create_user(payload)
    response = new_user.login(payload)
    yield response
    token = response.json()['accessToken']
    new_user.delete_user(payload, token)


@allure.step("Авторизация пользователя c неверным паролем и удаление его по окончании теста")
@pytest.fixture(scope='function')
def auth_incorrect():
    new_user = Auth()
    payload = new_user.create_payload()
    response = new_user.create_user(payload)
    token = response.json()['accessToken']
    payload['password'] = 'wwww1222'
    response_auth = new_user.login(payload)
    yield response_auth
    new_user.delete_user(payload, token)


@allure.step("Обновление данных авторизованного пользователя и удаление его по окончании теста")
@pytest.fixture(scope='function')
def update_user():
    new_user = Update()
    payload = new_user.create_payload()
    new_user.create_user(payload)
    response = new_user.login(payload)
    payload['name'] = 'Ivan'
    token = response.json()['accessToken']
    response = new_user.update(payload, token)
    yield response
    new_user.delete_user(payload, token)


@allure.step("Получение токена для создания заказа авторизованным пользователем и удаление его по окончании теста")
@pytest.fixture(scope='function')
def token():
    new_order = Orders()
    payload = new_order.create_payload()
    new_order.create_user(payload)
    response = new_order.login(payload)
    token = response.json()['accessToken']
    yield token
    new_order.delete_user(payload, token)
