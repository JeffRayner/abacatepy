import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SECRET_KEY": "test-secret",
    })

    with app.test_client() as client:
        yield client
