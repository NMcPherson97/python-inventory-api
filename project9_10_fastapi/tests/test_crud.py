import sqlite3
import pytest
from app import crud

@pytest.fixture
def test_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT,
            category TEXT,
            quantity INTEGER,
            price REAL,
            inventory_value REAL
        )
    """)
    conn.commit()
    yield conn
    conn.close()

def test_get_all_returns_list(test_db):
    result = crud.get_all_items(test_db)
    assert isinstance(result, list)

def test_get_nonexistent_returns_none(test_db):
    result = crud.get_item_by_id(test_db, 99999)
    assert result is None

def test_delete_nonexistent_returns_false(test_db):
    result = crud.delete_item(test_db, 99999)
    assert result == False