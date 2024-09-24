import pytest
import requests
x_clients_url = "https://x-clients-be.onrender.com"


@pytest.fixture()
def get_token(username="bloom", password="fire-fairy"):
    log_pass = {"username": username, "password": password}
    resp_token = requests.post(x_clients_url + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token