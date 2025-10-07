import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pixel_endpoint():
    r = client.get('/pixel/test-campaign/test-recipient.png')
    assert r.status_code == 200
    assert r.headers['content-type'] == 'image/png'

def test_redirect_endpoint():
    r = client.get('/r/test-campaign/test-recipient', allow_redirects=False)
    assert r.status_code == 302
