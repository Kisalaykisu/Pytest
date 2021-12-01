import requests

def test_twitter_is_present():
    resp = requests.get("http://www.yahoo.com/")
    assert "twitter" in resp.text 
