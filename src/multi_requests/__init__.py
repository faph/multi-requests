"""
multi-requests API
"""
import importlib.metadata
from typing import List, Union

import more_itertools
import requests

__version__ = importlib.metadata.version("multi-requests")


class MultiSession:
    """A HTTP client session supporting simultaneous requests"""

    def __init__(self):
        """A HTTP client session supporting simultaneous requests"""
        self._session = requests.Session()

    def get(self, url: Union[str, List[str]], **kwargs) -> List[requests.Response]:
        """Send a HTTP GET request"""
        all_kwargs = {"url": url, **kwargs}
        kwarg_values_sequence = more_itertools.zip_broadcast(
            *all_kwargs.values(), scalar_types=(str, bytes, dict)
        )
        responses = [
            self._session.get(**dict(zip(all_kwargs, values))) for values in kwarg_values_sequence
        ]
        return responses
