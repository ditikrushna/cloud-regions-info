from cloud_regions_info import get_region_info

def test_get_oci_region_info():
    """Test getting OCI region information."""
    region_info = get_region_info(provider="oci", region="us-ashburn-1")
    
    assert region_info["location"] == "Ashburn, VA"
    assert region_info["country"] == "United States"
    assert region_info["flag"] == "🇺🇸"
    assert region_info["latitude"] == 39.0438
    assert region_info["longitude"] == -77.4874
    assert region_info["raw"] == "us-ashburn-1"

def test_oci_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="oci", region="EU-FRANKFURT-1")
    assert region_info["location"] == "Frankfurt"
    assert region_info["country"] == "Germany"

def test_unknown_oci_region():
    """Test handling of unknown regions."""
    region_info = get_region_info(provider="oci", region="invalid-region")
    assert region_info["location"] == "Unknown"
    assert region_info["country"] == "Unknown"
    assert region_info["raw"] == "invalid-region"
    assert region_info["flag"] is None
    assert region_info["latitude"] is None
    assert region_info["longitude"] is None

def test_oci_regions_by_continent():
    """Test regions across different continents."""
    # North America
    region_info = get_region_info(provider="oci", region="us-phoenix-1")
    assert region_info["country"] == "United States"
    assert region_info["location"] == "Phoenix, AZ"

    # Europe
    region_info = get_region_info(provider="oci", region="uk-london-1")
    assert region_info["country"] == "United Kingdom"
    assert region_info["location"] == "London"

    # Asia
    region_info = get_region_info(provider="oci", region="ap-tokyo-1")
    assert region_info["country"] == "Japan"
    assert region_info["location"] == "Tokyo"

    # Middle East
    region_info = get_region_info(provider="oci", region="me-jeddah-1")
    assert region_info["country"] == "Saudi Arabia"
    assert region_info["location"] == "Jeddah"

def test_oci_additional_regions():
    """Test additional OCI regions."""
    # US Additional
    region_info = get_region_info(provider="oci", region="us-chicago-1")
    assert region_info["country"] == "United States"
    assert region_info["location"] == "Chicago, IL"

    # Europe Additional
    region_info = get_region_info(provider="oci", region="eu-paris-1")
    assert region_info["country"] == "France"
    assert region_info["location"] == "Paris"

    # Asia Pacific Additional
    region_info = get_region_info(provider="oci", region="ap-melbourne-1")
    assert region_info["country"] == "Australia"
    assert region_info["location"] == "Melbourne"

    # South America Additional
    region_info = get_region_info(provider="oci", region="sa-santiago-1")
    assert region_info["country"] == "Chile"
    assert region_info["location"] == "Santiago"

    # Mexico Region
    region_info = get_region_info(provider="oci", region="mx-queretaro-1")
    assert region_info["country"] == "Mexico"
    assert region_info["location"] == "Queretaro"

    # Israel Region
    region_info = get_region_info(provider="oci", region="il-jerusalem-1")
    assert region_info["country"] == "Israel"
    assert region_info["location"] == "Jerusalem" 