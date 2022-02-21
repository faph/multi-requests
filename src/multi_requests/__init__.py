"""
multi-requests API
"""

import importlib.metadata
from typing import List, Union

import requests

__version__ = importlib.metadata.version("multi-requests")


class MultiSession:
    """A HTTP client session supporting simultaneous requests"""

    def __init__(self):
        """A HTTP client session supporting simultaneous requests"""
        self._session = requests.Session()

    def get(self, url: Union[str, List[str]], **kwargs) -> requests.Response:
        """Send a HTTP GET request"""
        if isinstance(url, str):
            return self._session.get(url, **kwargs)
        else:
            return [self._session.get(single_url, **kwargs) for single_url in url]
