from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """
    Abstract base class for a cloud provider.
    """

    @abstractmethod
    def get_region_info(self, region: str) -> dict:
        """
        Returns a dictionary with the region information, e.g.:
        {
          "location": str,
          "flag": str,
          "country": str,
          "latitude": float,
          "longitude": float,
          "raw": str
        }
        """
        pass
