import pytest
from app import app
from database import db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.test_endpoints_get
def test_get_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data is not None

@pytest.mark.test_endpoints_get
def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert response.data is not None

@pytest.mark.test_endpoints_get
def test_get_inventory_create(client):
    response = client.get("/inventory/create")
    assert response.status_code == 200
    assert response.data is not None

@pytest.mark.test_endpoints_get
def test_get_inventory_delete(client):
    response = client.get("/inventory/delete")
    assert response.status_code == 200
    assert response.data is not None

@pytest.mark.test_endpoints_get
def test_get_inventory_success(client):
    response = client.get("/inventory/success")
    assert response.status_code == 200
    assert response.data is not None
    assert b'Inventory updated' in response.data

@pytest.mark.test_endpoints_post
def test_post_inventory_no_param(client):
    response = client.post("/inventory/create")
    assert response.status_code == 200
    assert response.data is not None
    assert b'Invalidad data in the form' in response.data

@pytest.mark.test_endpoints_post
def test_post_inventory_with_param(client):
    item = {
        "name": "Test object",
        "sell_in": 10,
        "quality": 5,
        "class_object":"ConjuredItem"
    }
    response = client.post("/inventory/create", data=item)
    assert response.status_code == 200
    assert response.data is not None
    assert b'Inventory updated' in response.data

@pytest.mark.test_endpoints_put
def test_put_inventory(client):
    response = client.put("/inventory")
    assert response.status_code == 200
    assert response.data is not None
    assert b'{"success":true}' in response.data

@pytest.mark.test_endpoints_delete
def test_delete_inventory_item(client):
    item_id = {
        "id": 1
    }
    response = client.delete("/inventory/delete", data=item_id)
    assert response.status_code == 200
    assert response.data is not None
    
    INVENTORY = db.get_all_inventory()
    id_item_list = [item['id'] for item in INVENTORY]
    
    assert 1 not in id_item_list
