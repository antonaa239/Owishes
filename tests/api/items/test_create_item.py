import allure

@allure.title("Успешное создание элемента")
def test_create_item(item_client, created_wishlist_id, item_data):
    with allure.step("Отправить POST /api/items/create"):
        response = item_client.create(created_wishlist_id, item_data)
    with allure.step("Проверить статус код"):
        assert response.status_code == 201
