import requests

def test_get_successful_response():
    resp = requests.get("http://www.yahoo.com/")
    assert resp.status_code == 200