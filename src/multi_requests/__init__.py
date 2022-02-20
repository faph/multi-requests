"""
multi-requests API
"""

import importlib.metadata

__version__ = importlib.metadata.version("multi-requests")


class MultiSession():
    """A HTTP client session supporting simultaneous requests"""
