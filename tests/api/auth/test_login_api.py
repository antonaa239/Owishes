import allure

@allure.title ("Успешный логин пользователя")
@allure.description("Попытка успешного логина пользователя")
def test_login(auth_client, user_data):
    with allure.step("Запрос POST /api/auth/login"):
        auth_client.register(user_data)
    with allure.step("Проверка статуса запроса"):
        response = auth_client.login(user_data["email"], user_data["password"])
        assert response.status_code == 200
