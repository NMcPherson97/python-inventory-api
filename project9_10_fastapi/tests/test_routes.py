from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_inventory():
    response = client.get("/inventory")
    assert response.status_code == 200

def test_get_item_not_found():
    response = client.get("/inventory/99999")
    assert response.status_code == 404

def test_post_missing_fields_returns_422():
    response = client.post("/inventory", json={})
    assert response.status_code == 422

def test_post_valid_item():
    response = client.post("/inventory", json={
        "item": "Test Item",
        "category": "Test",
        "quantity": 5,
        "price": 9.99
    })
    assert response.status_code == 201

def test_delete_nonexistent_returns_404():
    response = client.delete("/inventory/99999")
    assert response.status_code == 404

def test_analytics_category_totals():
    response = client.get("/analytics/category_totals")
    assert response.status_code == 200

def test_analytics_highest_value():
    response = client.get("/analytics/highest_value_item")
    assert response.status_code == 200

def test_analytics_total_value():
    response = client.get("/analytics/total_inventory_value")
    assert response.status_code == 200