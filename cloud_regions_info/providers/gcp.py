from .base import BaseProvider

class GCPProvider(BaseProvider):
    def get_region_info(self, region: str) -> dict:
        """
        Return region metadata in the form of a dictionary derived from a RegionInfo model.
        """
        raise NotImplementedError("GCP provider not implemented yet.")
