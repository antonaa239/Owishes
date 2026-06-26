import allure
import pytest

negative_cases = [
    ({
        "email":"test@test.ru",
        "password":"12",
        "name":"valid"
    }, 400),
    ({
        "email":"invalidemail",
        "password":"12345678",
        "name":"valid"
    }, 422)
]

def test_register(auth_client, user_data):
    response = auth_client.register(user_data)
    assert response.status_code == 201

@pytest.mark.parametrize("invalid_user_data, expected_status", negative_cases)
def test_register_negative(auth_client, invalid_user_data, expected_status):
    response = auth_client.register(invalid_user_data)
    assert response.status_code == expected_status