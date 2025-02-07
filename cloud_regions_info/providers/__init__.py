"""
providers/__init__.py

Defines how we select the correct provider class for a given provider string.
"""

from .base import BaseProvider
from .aws import AWSProvider
from .azure import AzureProvider
from .gcp import GCPProvider
from .oci import OCIProvider
from .digitalocean import DigitalOceanProvider

PROVIDER_MAP = {
    "aws": AWSProvider,
    "azure": AzureProvider,
    "gcp": GCPProvider,
    "oci": OCIProvider,
    "digitalocean": DigitalOceanProvider
}

def get_provider(provider_name: str) -> BaseProvider:
    """
    Returns an instance of the provider class for the given provider name.
    """
    key = provider_name.strip().lower()
    if key not in PROVIDER_MAP:
        raise ValueError(f"Provider '{provider_name}' is not supported.")
    return PROVIDER_MAP[key]()
