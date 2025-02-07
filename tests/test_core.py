from cloud_regions_info import get_region_info

def test_core_aws_known():
    data = get_region_info("AWS", "eu-north-1")
    assert data["location"] == "Europe (Stockholm)"
    assert data["flag"] == "🇸🇪"
    assert data["country"] == "Sweden"
    assert data["raw"] == "eu-north-1"

def test_core_aws_unknown():
    data = get_region_info("AWS", "non-existent-999")
    assert data["location"] == "Unknown"
    assert data["country"] == "Unknown"
    assert data["raw"] == "non-existent-999"
