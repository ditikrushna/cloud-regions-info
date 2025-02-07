from cloud_regions_info import get_region_info

def test_get_vultr_region_info():
    """Test getting Vultr Cloud region information."""
    region_info = get_region_info(provider="vultr", region="ewr")
    
    assert region_info["location"] == "New Jersey"
    assert region_info["country"] == "United States"
    assert region_info["flag"] == "🇺🇸"
    assert region_info["latitude"] == 40.7128
    assert region_info["longitude"] == -74.0060
    assert region_info["raw"] == "ewr"

def test_vultr_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="vultr", region="LHR")
    assert region_info["location"] == "London"
    assert region_info["country"] == "United Kingdom"

def test_unknown_vultr_region():
    """Test handling of unknown regions."""
    region_info = get_region_info(provider="vultr", region="invalid-region")
    assert region_info["location"] == "Unknown"
    assert region_info["country"] == "Unknown"
    assert region_info["raw"] == "invalid-region"
    assert region_info["flag"] is None
    assert region_info["latitude"] is None
    assert region_info["longitude"] is None

def test_vultr_us_regions():
    """Test US regions."""
    regions = {
        "ewr": "New Jersey",
        "ord": "Chicago",
        "dfw": "Dallas",
        "sea": "Seattle",
        "lax": "Los Angeles",
        "atl": "Atlanta"
    }
    
    for region, city in regions.items():
        region_info = get_region_info(provider="vultr", region=region)
        assert region_info["country"] == "United States"
        assert region_info["location"] == city
        assert region_info["flag"] == "🇺🇸"

def test_vultr_europe_regions():
    """Test European regions."""
    regions = {
        "ams": ("Amsterdam", "Netherlands", "🇳🇱"),
        "lhr": ("London", "United Kingdom", "🇬🇧"),
        "fra": ("Frankfurt", "Germany", "🇩🇪"),
        "par": ("Paris", "France", "🇫🇷"),
        "waw": ("Warsaw", "Poland", "🇵🇱"),
        "mad": ("Madrid", "Spain", "🇪🇸")
    }
    
    for region, (city, country, flag) in regions.items():
        region_info = get_region_info(provider="vultr", region=region)
        assert region_info["location"] == city
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_vultr_asia_pacific():
    """Test Asia Pacific regions."""
    regions = {
        "nrt": ("Tokyo", "Japan", "🇯🇵"),
        "icn": ("Seoul", "South Korea", "🇰🇷"),
        "sgp": ("Singapore", "Singapore", "🇸🇬"),
        "syd": ("Sydney", "Australia", "🇦🇺"),
        "blr": ("Bangalore", "India", "🇮🇳")
    }
    
    for region, (city, country, flag) in regions.items():
        region_info = get_region_info(provider="vultr", region=region)
        assert region_info["location"] == city
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_vultr_other_regions():
    """Test regions in other continents."""
    # Mexico
    region_info = get_region_info(provider="vultr", region="mex")
    assert region_info["country"] == "Mexico"
    assert region_info["location"] == "Mexico City"
    assert region_info["flag"] == "🇲🇽"

    # South Africa
    region_info = get_region_info(provider="vultr", region="jnb")
    assert region_info["country"] == "South Africa"
    assert region_info["location"] == "Johannesburg"
    assert region_info["flag"] == "🇿🇦"

    # Israel
    region_info = get_region_info(provider="vultr", region="tel")
    assert region_info["country"] == "Israel"
    assert region_info["location"] == "Tel Aviv"
    assert region_info["flag"] == "🇮🇱" 