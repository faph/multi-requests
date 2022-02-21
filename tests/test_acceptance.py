import pytest

import multi_requests


@pytest.fixture
def session():
    return multi_requests.MultiSession()


def test_has_version():
    assert multi_requests.__version__


def test_multiple_urls_return_responses(session):
    urls = ["https://catfact.ninja/facts", "https://catfact.ninja/breeds"]
    responses = session.get(urls)
    assert len(responses) == 2


def test_multiple_urls_with_single_params_return_responses(session):
    urls = [
        "https://catfact.ninja/facts",
        "https://catfact.ninja/facts",
    ]
    params = [
        {"max_length": 100},
        {"limit": 2},
    ]
    responses = session.get(urls, params=params)
    assert len(responses) == 2


def test_multiple_params_return_responses(session):
    url = "https://catfact.ninja/facts"
    params = {"max_length": 100}
    responses = session.get(urls, params=params)
    assert len(responses) == 2


def test_multiple_urls_and_params_return_responses(session):
    urls = [
        "https://catfact.ninja/facts",
        "https://catfact.ninja/breeds",
    ]
    params = [
        {"max_length": 100},
        {"limit": 2},
    ]
    responses = session.get(urls, params=params)
    assert len(responses) == 2
