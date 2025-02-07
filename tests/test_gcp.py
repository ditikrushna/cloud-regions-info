from cloud_regions_info import get_region_info

def test_get_gcp_region_info():
    """Test getting GCP region information."""
    region_info = get_region_info(provider="gcp", region="us-central1")
    
    assert region_info["location"] == "Iowa"
    assert region_info["country"] == "United States"
    assert region_info["flag"] == "🇺🇸"
    assert region_info["latitude"] == 41.878113
    assert region_info["longitude"] == -93.097702
    assert region_info["raw"] == "us-central1"

def test_gcp_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="gcp", region="EUROPE-WEST1")
    assert region_info["location"] == "Belgium"
    assert region_info["country"] == "Belgium"

def test_unknown_gcp_region():
    """Test handling of unknown regions."""
    region_info = get_region_info(provider="gcp", region="invalid-region")
    assert region_info["location"] == "Unknown"
    assert region_info["country"] == "Unknown"
    assert region_info["raw"] == "invalid-region"
    assert region_info["flag"] is None
    assert region_info["latitude"] is None
    assert region_info["longitude"] is None

def test_gcp_regions_by_continent():
    """Test regions across different continents."""
    # North America
    region_info = get_region_info(provider="gcp", region="us-west2")
    assert region_info["country"] == "United States"
    assert region_info["location"] == "Los Angeles"

    # Europe
    region_info = get_region_info(provider="gcp", region="europe-west3")
    assert region_info["country"] == "Germany"
    assert region_info["location"] == "Frankfurt"

    # Asia
    region_info = get_region_info(provider="gcp", region="asia-northeast1")
    assert region_info["country"] == "Japan"
    assert region_info["location"] == "Tokyo"

    # Australia
    region_info = get_region_info(provider="gcp", region="australia-southeast1")
    assert region_info["country"] == "Australia"
    assert region_info["location"] == "Sydney"

    # South America
    region_info = get_region_info(provider="gcp", region="southamerica-east1")
    assert region_info["country"] == "Brazil"
    assert region_info["location"] == "São Paulo" 