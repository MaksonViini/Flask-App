from django.http import response
import pytest
import httpx

def test_hello():
    response = httpx.get('http://localhost:5000/api/hello')
    assert response.status_code == 200
    assert response.json() == {'hello': 'world'}