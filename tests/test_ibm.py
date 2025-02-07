from cloud_regions_info import get_region_info

def test_get_ibm_region_info():
    """Test getting IBM Cloud region information."""
    region_info = get_region_info(provider="ibm", region="us-south")
    
    assert region_info["location"] == "Dallas"
    assert region_info["country"] == "United States"
    assert region_info["flag"] == "🇺🇸"
    assert region_info["latitude"] == 32.7767
    assert region_info["longitude"] == -96.7970
    assert region_info["raw"] == "us-south"

def test_ibm_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="ibm", region="EU-GB")
    assert region_info["location"] == "London"
    assert region_info["country"] == "United Kingdom"

def test_unknown_ibm_region():
    """Test handling of unknown regions."""
    region_info = get_region_info(provider="ibm", region="invalid-region")
    assert region_info["location"] == "Unknown"
    assert region_info["country"] == "Unknown"
    assert region_info["raw"] == "invalid-region"
    assert region_info["flag"] is None
    assert region_info["latitude"] is None
    assert region_info["longitude"] is None

def test_ibm_regions_by_continent():
    """Test regions across different continents."""
    # North America
    region_info = get_region_info(provider="ibm", region="ca-tor")
    assert region_info["country"] == "Canada"
    assert region_info["location"] == "Toronto"

    # Europe
    region_info = get_region_info(provider="ibm", region="eu-de")
    assert region_info["country"] == "Germany"
    assert region_info["location"] == "Frankfurt"

    # Asia
    region_info = get_region_info(provider="ibm", region="jp-tok")
    assert region_info["country"] == "Japan"
    assert region_info["location"] == "Tokyo"

    # Oceania
    region_info = get_region_info(provider="ibm", region="au-syd")
    assert region_info["country"] == "Australia"
    assert region_info["location"] == "Sydney"

def test_ibm_japan_regions():
    """Test multiple regions in Japan."""
    regions = {
        "jp-tok": "Tokyo",
        "jp-osa": "Osaka"
    }
    
    for region, city in regions.items():
        region_info = get_region_info(provider="ibm", region=region)
        assert region_info["country"] == "Japan"
        assert region_info["location"] == city
        assert region_info["flag"] == "🇯🇵"

def test_ibm_multizone_regions():
    """Test multiple zones in same region."""
    # Dallas zones
    for region in ["us-south", "us-south-2", "us-south-3"]:
        region_info = get_region_info(provider="ibm", region=region)
        assert region_info["country"] == "United States"
        assert "Dallas" in region_info["location"]
        assert region_info["flag"] == "🇺🇸"

def test_ibm_europe_regions():
    """Test European regions."""
    regions = {
        "eu-gb": ("London", "United Kingdom", "🇬🇧"),
        "eu-de": ("Frankfurt", "Germany", "🇩🇪"),
        "eu-es": ("Madrid", "Spain", "🇪🇸"),
        "eu-fr2": ("Paris", "France", "🇫🇷"),
        "eu-it1": ("Milan", "Italy", "🇮🇹")
    }
    
    for region, (city, country, flag) in regions.items():
        region_info = get_region_info(provider="ibm", region=region)
        assert region_info["location"] == city
        assert region_info["country"] == country
        assert region_info["flag"] == flag 