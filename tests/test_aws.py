from cloud_regions_info.providers.aws import AWSProvider

def test_aws_us_east_1():
    provider = AWSProvider()
    data = provider.get_region_info("us-east-1")
    assert data["location"] == "US East (N. Virginia)"
    assert data["country"] == "United States"
    assert data["flag"] == "🇺🇸"
    assert abs(data["latitude"] - 39.028760) < 1e-6
    assert abs(data["longitude"] + 77.458263) < 1e-6

def test_aws_eu_north_1():
    provider = AWSProvider()
    data = provider.get_region_info("eu-north-1")
    assert data["location"] == "Europe (Stockholm)"
    assert data["flag"] == "🇸🇪"
    assert data["country"] == "Sweden"

def test_aws_us_east_2():
    provider = AWSProvider()
    data = provider.get_region_info("us-east-2")
    assert data["location"] == "US East (Ohio)"
    assert data["flag"] == "🇺🇸"
    assert data["country"] == "United States"
