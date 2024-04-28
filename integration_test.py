# Imports
from app import create_app, User

# Integration tests
def test_user_registration():
  app = create_app('testing')  # Create app in testing mode
  with app.app_context():
    # Create a user
    user = User(username="test_user", email="test@example.com", password="password")
    db.session.add(user)
    db.session.commit()

    # Check if user is registered
    registered_user = User.query.filter_by(username="test_user").first()
    assert registered_user is not None

# Clean up after tests (optional)
def teardown_module():
  # Drop tables or clear data after all tests
  pass
