import pytest
from endpoints.registration import Registration
from endpoints.auth import Auth
import allure



@allure.step("Создание нового пользователя, возвращение payload и response")
@pytest.fixture(scope='function')
def payload():
    new_user = Registration()
    payload = new_user.create_payload()
    response = new_user.create_user(payload)
    token = response.json()['accessToken']
    yield (payload, response)
    new_user.delete_user(payload, token)


@allure.step("Авторизация пользователя, возвращение token, response, payload")
@pytest.fixture(scope='function')
def auth_token():
    new_order = Auth()
    payload = new_order.create_payload()
    new_order.create_user(payload)
    response = new_order.login(payload)
    token = response.json()['accessToken']
    yield (token, response, payload)
    new_order.delete_user(payload, token)










