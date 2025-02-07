from cloud_regions_info import get_region_info

def test_get_digitalocean_region_info():
    """Test getting DigitalOcean region information."""
    region_info = get_region_info(provider="digitalocean", region="nyc1")
    
    assert region_info["location"] == "New York City"
    assert region_info["country"] == "United States"
    assert region_info["flag"] == "🇺🇸"
    assert region_info["latitude"] == 40.7128
    assert region_info["longitude"] == -74.0060
    assert region_info["raw"] == "nyc1"

def test_digitalocean_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="digitalocean", region="AMS3")
    assert region_info["location"] == "Amsterdam"
    assert region_info["country"] == "Netherlands"

def test_unknown_digitalocean_region():
    """Test handling of unknown regions."""
    region_info = get_region_info(provider="digitalocean", region="invalid-region")
    assert region_info["location"] == "Unknown"
    assert region_info["country"] == "Unknown"
    assert region_info["raw"] == "invalid-region"
    assert region_info["flag"] is None
    assert region_info["latitude"] is None
    assert region_info["longitude"] is None

def test_digitalocean_regions_by_continent():
    """Test regions across different continents."""
    # North America
    region_info = get_region_info(provider="digitalocean", region="sfo3")
    assert region_info["country"] == "United States"
    assert region_info["location"] == "San Francisco"

    # Europe
    region_info = get_region_info(provider="digitalocean", region="fra1")
    assert region_info["country"] == "Germany"
    assert region_info["location"] == "Frankfurt"

    # Asia
    region_info = get_region_info(provider="digitalocean", region="sgp1")
    assert region_info["country"] == "Singapore"
    assert region_info["location"] == "Singapore"

    # Oceania
    region_info = get_region_info(provider="digitalocean", region="syd1")
    assert region_info["country"] == "Australia"
    assert region_info["location"] == "Sydney"

def test_digitalocean_multiple_regions_same_location():
    """Test multiple regions in the same location."""
    # Singapore regions
    for region in ["sgp1", "sin1", "sin2", "sin3"]:
        region_info = get_region_info(provider="digitalocean", region=region)
        assert region_info["country"] == "Singapore"
        assert region_info["location"] == "Singapore"
        assert region_info["flag"] == "🇸🇬"

    # Sydney regions
    for region in ["syd1", "syd2", "syd3"]:
        region_info = get_region_info(provider="digitalocean", region=region)
        assert region_info["country"] == "Australia"
        assert region_info["location"] == "Sydney"
        assert region_info["flag"] == "🇦🇺"

    # Bangalore regions
    for region in ["blr1", "blr2", "blr3"]:
        region_info = get_region_info(provider="digitalocean", region=region)
        assert region_info["country"] == "India"
        assert region_info["location"] == "Bangalore"
        assert region_info["flag"] == "🇮🇳"

def test_digitalocean_india_regions():
    """Test all regions in India."""
    region_mappings = {
        "blr1": "Bangalore",
        "maa1": "Chennai",
        "del1": "Delhi"
    }
    
    for region, city in region_mappings.items():
        region_info = get_region_info(provider="digitalocean", region=region)
        assert region_info["country"] == "India"
        assert region_info["location"] == city
        assert region_info["flag"] == "🇮🇳" 