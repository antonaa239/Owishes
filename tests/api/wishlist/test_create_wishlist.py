import allure

@allure.title("Создание вишлиста")
@allure.description("Тестируем корректное создание вишлиста")
def test_create_wishlist(wishlist_client, wishlist_data):
    with allure.step("Запрос POST api/wishlist/create"):
        response = wishlist_client.create(wishlist_data)
    with allure.step("Проверка статуса запроса"):
        assert response.status_code == 201
    with allure.step("Проверка наличия поля id"):
        allure.attach(name="response text", body=response.text, attachment_type=allure.attachment_type.JSON)
        json_data = response.json()
        assert "id" in json_data
