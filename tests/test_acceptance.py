import multi_requests

def test_has_version():
    assert multi_requests.__version__

def test_multiple_urls_return_responses():
    session = multi_requests.MultiSession()
    urls = ["https://catfact.ninja/facts", "https://catfact.ninja/breeds"]
    responses = session.get(urls)
    assert len(responses) == 2

def test_multiple_params_return_responses():
    session = multi_requests.MultiSession()
    url = "https://catfact.ninja/facts"
    params = [
        {"max_length": 100},
        {"max_length": 200},
    ]
    responses = session.get(url, params=params)
    assert len(responses) == 2
