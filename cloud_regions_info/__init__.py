"""
cloud_regions_info
~~~~~~~~~~~~~~~~~~

A Python package for retrieving cloud region information.
Currently supports AWS in a full-fledged manner, with placeholders for Azure & GCP.
"""

__version__ = "0.1.0"

# Expose a single function from core
from .core import get_region_info
