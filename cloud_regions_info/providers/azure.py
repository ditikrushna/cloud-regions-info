from .base import BaseProvider

class AzureProvider(BaseProvider):
    def get_region_info(self, region: str) -> dict:
        """
        Return region metadata in the form of a dictionary derived from a RegionInfo model.
        """
        raise NotImplementedError("Azure provider not implemented yet.")
