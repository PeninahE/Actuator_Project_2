#test_app_routes.py

def test_hello(client):
    response = client.get("/hello")
    assert b"hello world" in response.data
def test_app_html(client):
    response = client.get("/")
    assert b"Welcome to my project!" in response.data


def test_actuator (client):
    actuator_response = client.post('/actuator', data={'status': 'health'})
    assert b"UP" in actuator_response.data

