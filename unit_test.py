# Imports
from app import User, LoginForm, RegisterForm

# Unit tests for User model
def test_user_init(app):
  with app.app_context():
    user = User(username="test_user", email="test@example.com", password="password")
    assert user.username == "test_user"
    assert user.email == "test@example.com"
    assert user.password_hash is not None  # Password is hashed

# Unit tests for forms
def test_login_form_validation():
  form = LoginForm()
  assert not form.validate_on_submit()  # Empty form fails validation

  form.username.data = "test_user"
  assert not form.validate_on_submit()  # Password required

  form.password.data = "password"
  assert form.validate_on_submit()  # Valid form

def test_register_form_validation():
  form = RegisterForm()
  assert not form.validate_on_submit()  # Empty form fails validation

  # Add tests for username uniqueness, email format, password confirmation, etc.
