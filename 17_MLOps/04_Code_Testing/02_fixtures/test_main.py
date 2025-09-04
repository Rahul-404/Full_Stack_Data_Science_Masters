import pytest 
from main import UserManager

@pytest.fixture
def user_manager():
    """Fixture to create a UserManager instance."""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("rahul_shelke", "rahulshelke@example.com") == True
    assert user_manager.get_user("rahul_shelke") == "rahulshelke@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("rahul_shelke", "rahulshelke@example.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("rahul_shelke", "another@example.com")