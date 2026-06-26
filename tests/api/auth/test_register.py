import allure
import pytest

negative_cases = [
    ({
        "email":"test@test.ru",
        "password":"12",
        "name":"valid"
    }, 400, "паролем"),
    ({
        "email":"invalidemail",
        "password":"12345678",
        "name":"valid"
    }, 422, "email")
]

@allure.title("Успешная регистрация пользователя")
@allure.description("Пользователь регистрируется с валидными данными")
def test_register(auth_client, user_data):
    with allure.step("Запрос POST /api/auth/register"):
        response = auth_client.register(user_data)
    with allure.step("Проверка статус-кода"):
        assert response.status_code == 201

@pytest.mark.parametrize("invalid_user_data, expected_status, test_case_title", negative_cases)
def test_register_negative(auth_client, invalid_user_data, expected_status, test_case_title):
    allure.dynamic.title("Негативный сценарий: невалидный " + test_case_title)
    allure.dynamic.description("Попытка регистрации с невалидным " + test_case_title)
    with allure.step("Запрос POST /api/auth/regist с невалидным " + test_case_title):
        response = auth_client.register(invalid_user_data)
    with allure.step("Проверка статуса"):
        assert response.status_code == expected_status