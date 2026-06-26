def test_create_item(item_client, created_wishlist_id, item_data):
    response = item_client.create(created_wishlist_id, item_data)
    assert response.status_code == 201
