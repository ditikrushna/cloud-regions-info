import os
import json
from .base import BaseProvider
from ..models import RegionInfo

class AWSProvider(BaseProvider):
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_path, "..", "mappings", "aws_regions.json")
        with open(data_path, "r", encoding="utf-8") as f:
            self.region_data = json.load(f)

    def get_region_info(self, region: str) -> dict:
        """
        Return region metadata in the form of a dictionary derived from a RegionInfo model.
        """
        info = self.region_data.get(region, {})
        if not info:
            model = RegionInfo(
                location="Unknown",
                country="Unknown",
                raw=region
            )
            return model.dict()
        model = RegionInfo(
            location=info.get("location", "Unknown"),
            flag=info.get("flag", None),
            country=info.get("country", "Unknown"),
            latitude=info.get("latitude", None),
            longitude=info.get("longitude", None),
            raw=region
        )
        return model.dict()
