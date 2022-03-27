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
        """
        Send a HTTP GET request

        Follows same API as :meth:`requests.Session.get` except that arguments can be lists. Each
        value in such a list would correspond to a single request. If multiple (keyword) arguments
        are lists they must have the same length.
        """
        all_kwargs = {"url": url, **kwargs}
        # Broadcast scalar kwarg values to same length as list kwargs
        kwarg_values_sequence = more_itertools.zip_broadcast(
            *all_kwargs.values(),
            scalar_types=(str, bytes, dict),
            strict=True,
        )
        # Combine with the kwarg keys
        kwarg_dicts_sequence = (dict(zip(all_kwargs, values)) for values in kwarg_values_sequence)
        responses = [self._session.get(**kwarg_dict) for kwarg_dict in kwarg_dicts_sequence]
        return responses
