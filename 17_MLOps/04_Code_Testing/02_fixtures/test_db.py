import pytest 
from db import Database

@pytest.fixture
def db():
    """Provides a fresh instance of the Database class and cleans up after the test."""
    databse = Database()
    yield databse # Provide the fixture instance
    databse.data.clear() # CLeanup step (not needed for in-memory, but useful for real DBs)

def test_add_user(db):
    db.add_user(1, "Rahul")
    assert db.get_user(1) == "Rahul"

def test_add_duplicate_user(db):
    db.add_user(1, "Rahul")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Shelke")

def test_delete_user(db):
    db.add_user(2, "Shelke")
    db.delete_user(2)
    assert db.get_user(2) is None