"""
multi-requests API
"""
import functools
import importlib.metadata
from typing import Any, List, Union

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
        # Arguments that are shared and apply to all requests
        common_kwargs = {
            param: value for param, value in all_kwargs.items() if not _is_sequence(value)
        }
        # Arguments for which there is a different value for each request
        sequence_kwargs = {
            param: value for param, value in all_kwargs.items() if _is_sequence(value)
        }
        # Group them into a list, each item containing the kwargs for individual requests
        sequence_kwargs_list = [
            dict(zip(sequence_kwargs, group)) for group in list(zip(*sequence_kwargs.values()))
        ]
        request_fn = functools.partial(self._session.get, **common_kwargs)
        responses = [request_fn(**request_kwargs) for request_kwargs in sequence_kwargs_list]
        return responses


def _is_sequence(value: Any) -> bool:
    """Return whether a given parameter value is a sequence or not"""
    return isinstance(value, list)  # TODO: improve
