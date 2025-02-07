import pytest
from cloud_regions_info import get_region_info

def test_azure_region_info():
    """Test getting Azure region information."""
    region_info = get_region_info(provider="azure", region="eastus")
    
    assert region_info.location == "East US"
    assert region_info.country == "United States"
    assert region_info.flag == "🇺🇸"
    assert region_info.latitude == 37.3719
    assert region_info.longitude == -79.8164
    assert region_info.raw == "eastus"

def test_azure_region_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="azure", region="WestEurope")
    assert region_info.location == "West Europe"
    assert region_info.country == "Netherlands"

def test_invalid_azure_region():
    """Test that invalid regions raise an error."""
    with pytest.raises(ValueError, match="Azure region 'invalid-region' not found"):
        get_region_info(provider="azure", region="invalid-region")

def test_azure_european_regions():
    """Test European Azure regions."""
    region_info = get_region_info(provider="azure", region="francecentral")
    assert region_info.country == "France"
    assert region_info.flag == "🇫🇷"

    region_info = get_region_info(provider="azure", region="germanywestcentral")
    assert region_info.country == "Germany"
    assert region_info.flag == "🇩🇪"

def test_azure_asia_regions():
    """Test Asian Azure regions."""
    region_info = get_region_info(provider="azure", region="koreacentral")
    assert region_info.country == "South Korea"
    assert region_info.flag == "🇰🇷"

    region_info = get_region_info(provider="azure", region="uaenorth")
    assert region_info.country == "United Arab Emirates"
    assert region_info.flag == "🇦🇪"

def test_azure_special_regions():
    """Test regions with special characters in names."""
    region_info = get_region_info(provider="azure", region="chinanorth")
    assert region_info.country == "China"
    assert region_info.flag == "🇨🇳"

    region_info = get_region_info(provider="azure", region="southafricanorth")
    assert region_info.country == "South Africa"
    assert region_info.flag == "🇿🇦"

def test_azure_nordic_regions():
    """Test Nordic Azure regions."""
    region_info = get_region_info(provider="azure", region="swedencentral")
    assert region_info.country == "Sweden"
    assert region_info.flag == "🇸🇪"

def test_azure_latin_america_regions():
    """Test Latin American Azure regions."""
    region_info = get_region_info(provider="azure", region="mexicocentral")
    assert region_info.country == "Mexico"
    assert region_info.flag == "🇲🇽"

    region_info = get_region_info(provider="azure", region="chilecentral")
    assert region_info.country == "Chile"
    assert region_info.flag == "🇨🇱"

def test_azure_southeast_asia_regions():
    """Test Southeast Asian Azure regions."""
    region_info = get_region_info(provider="azure", region="malaysiawest")
    assert region_info.country == "Malaysia"
    assert region_info.flag == "🇲🇾"

    region_info = get_region_info(provider="azure", region="indonesiacentral")
    assert region_info.country == "Indonesia"
    assert region_info.flag == "🇮🇩"

def test_azure_australia_regions():
    """Test Australian Azure regions."""
    region_info = get_region_info(provider="azure", region="australiacentral")
    assert region_info.country == "Australia"
    assert region_info.flag == "🇦🇺"

    region_info = get_region_info(provider="azure", region="australiacentral2")
    assert region_info.country == "Australia"
    assert region_info.flag == "🇦🇺"

def test_azure_china_regions():
    """Test Chinese Azure regions."""
    region_info = get_region_info(provider="azure", region="chinaeast2")
    assert region_info.country == "China"
    assert region_info.flag == "🇨🇳"

    region_info = get_region_info(provider="azure", region="chinanorth3")
    assert region_info.country == "China"
    assert region_info.flag == "🇨🇳"

def test_azure_india_regions():
    """Test Indian Azure regions."""
    region_info = get_region_info(provider="azure", region="jioindiawest")
    assert region_info.country == "India"
    assert region_info.flag == "🇮🇳"

    region_info = get_region_info(provider="azure", region="jioindiacentral")
    assert region_info.country == "India"
    assert region_info.flag == "🇮🇳"