#test_app_routes.py

def test_hello(client):
    response = client.get("/hello")
    assert b"hello world" in response.data
def test_app_html(client):
    response = client.get("/")
    assert b"Welcome to my project!" in response.data


def test_actuator_health (client):
    actuator_response = client.post('/actuator', data={'status': 'health'})
    assert b"UP" in actuator_response.data


def test_actuator_env (client):
    actuator_response = client.post('/actuator', data={'status': 'env'})
    assert b"activeProfiles" in actuator_response.data
    assert b"propertySources" in actuator_response.data
    assert b"systemEnvironment" in actuator_response.data

#{"activeProfiles":[],"propertySources":[{"name":"systemEnvironment","properties":{"PATH":