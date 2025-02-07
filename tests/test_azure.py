from cloud_regions_info import get_region_info

def test_get_azure_region_info():
    """Test getting Azure region information."""
    region_info = get_region_info(provider="azure", region="eastus")
    
    assert region_info["location"] == "East US"
    assert region_info["country"] == "United States"
    assert region_info["flag"] == "🇺🇸"
    assert region_info["latitude"] == 37.3719
    assert region_info["longitude"] == -79.8164
    assert region_info["raw"] == "eastus"

def test_azure_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="azure", region="WestEurope")
    assert region_info["location"] == "West Europe"
    assert region_info["country"] == "Netherlands"

def test_unknown_azure_region():
    """Test handling of unknown regions."""
    region_info = get_region_info(provider="azure", region="invalid-region")
    assert region_info["location"] == "Unknown"
    assert region_info["country"] == "Unknown"
    assert region_info["raw"] == "invalid-region"
    assert region_info["flag"] is None
    assert region_info["latitude"] is None
    assert region_info["longitude"] is None

def test_azure_regions_by_continent():
    """Test regions across different continents."""
    # Europe
    region_info = get_region_info(provider="azure", region="francecentral")
    assert region_info["country"] == "France"
    assert region_info["flag"] == "🇫🇷"

    # Asia
    region_info = get_region_info(provider="azure", region="koreacentral")
    assert region_info["country"] == "South Korea"
    assert region_info["flag"] == "🇰🇷"

    # Americas
    region_info = get_region_info(provider="azure", region="brazilsouth")
    assert region_info["country"] == "Brazil"
    assert region_info["flag"] == "🇧🇷"

    # Africa
    region_info = get_region_info(provider="azure", region="southafricanorth")
    assert region_info["country"] == "South Africa"
    assert region_info["flag"] == "🇿🇦"

    # Oceania
    region_info = get_region_info(provider="azure", region="australiaeast")
    assert region_info["country"] == "Australia"
    assert region_info["flag"] == "🇦🇺"

def test_azure_special_regions():
    """Test special region types."""
    # Sovereign cloud
    region_info = get_region_info(provider="azure", region="chinanorth")
    assert region_info["country"] == "China"
    assert region_info["flag"] == "🇨🇳"

    # Partner regions
    region_info = get_region_info(provider="azure", region="westindia")
    assert region_info["country"] == "India"
    assert region_info["flag"] == "🇮🇳"
