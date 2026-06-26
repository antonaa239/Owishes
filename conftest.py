import pytest

from clients.auth_client import AuthClient
from clients.item_client import ItemClient
from clients.reservation_client import ReservationClient
from clients.wishlist_client import WishlistClient
from config import Config
from faker import Faker

from fixtures.auth_fixtures import item_data

fake = Faker()

pytest_plugins = [
    "fixtures.auth_fixtures",
]

@pytest.fixture
def auth_client():
    return AuthClient()

@pytest.fixture
def wishlist_client():
    return WishlistClient()

@pytest.fixture
def item_client():
    return ItemClient()

@pytest.fixture
def reservation_client():
    return ReservationClient()

@pytest.fixture(scope="session")
def created_wishlist_id():
    client = WishlistClient()
    response = client.create({
        "title": "session_wishlist",
        "description": "created by session fixture",
        "event_date": fake.future_date().isoformat()
    })
    assert response.status_code == 201, (
        f"Не удалось создать wishlist в session fixture: "
        f"{response.status_code} {response.text}"
    )
    wishlist_id = response.json()["id"]
    Config.WISHLIST_ID = wishlist_id
    return wishlist_id

@pytest.fixture(scope="session")
def created_item_id(created_wishlist_id):
    client = ItemClient()
    data = {
        "title": "test_title",
        "url": fake.url(),
        "price": fake.random_number(digits=4),
        "priority": "low",
        "note": "test_note"
    }
    response = client.create(created_wishlist_id, data)
    assert response.status_code == 201, (
        f"Не удалось создать wishlist в session fixture: "
        f"{response.status_code} {response.text}"
    )
    item_id = response.json()["id"]
    Config.ITEM_ID = item_id
    return item_id
