import multi_requests

def test_has_version():
    assert multi_requests.__version__

def test_multiple_urls_return_responses():
    session = multi_requests.MultiSession()
    urls = ["", ""]
    responses = session.get(urls)
    assert len(responses) == 2
