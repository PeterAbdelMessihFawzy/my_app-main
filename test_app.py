import pytest
from app import create_app, db
from app.models import User

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../users.db'  # Adjust the path to your database file
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_index_route(test_app):
    client = test_app.test_client()
    response = client.get('/')
    assert response.status_code == 302  # Check if the user is redirected to the login page when not logged in

def test_login(test_app):
    client = test_app.test_client()
    response = client.post('/login', data=dict(username='test_user', password='password'), follow_redirects=True)
    assert response.status_code == 200  # Check if the login page loads successfully after logging in

# Add more test functions for other routes and functionalities
