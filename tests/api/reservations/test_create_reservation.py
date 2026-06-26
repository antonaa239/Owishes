import allure

@allure.title("Успешная бронь предмета")
def test_create_item(reservation_client, created_item_id, reservation_data):
    with allure.step("Отправить запрос POST /api/resevations/"):
        response = reservation_client.create(created_item_id, reservation_data)
    with allure.step("Проверка статус кода"):
        assert response.status_code == 201
