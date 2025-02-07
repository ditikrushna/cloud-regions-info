"""
providers/__init__.py

Defines how we select the correct provider class for a given provider string.
"""

from .base import BaseProvider
from .aws import AWSProvider
from .azure import AzureProvider
from .gcp import GCPProvider

PROVIDER_MAP = {
    "aws": AWSProvider,
    "azure": AzureProvider,
    "gcp": GCPProvider
}

def get_provider(provider_name: str) -> BaseProvider:
    """
    Returns an instance of the provider class for the given provider name.
    """
    key = provider_name.strip().lower()
    if key not in PROVIDER_MAP:
        raise ValueError(f"Provider '{provider_name}' is not supported.")
    return PROVIDER_MAP[key]()
