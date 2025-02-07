from cloud_regions_info import get_region_info

def test_get_onedrive_region_info():
    """Test getting OneDrive region information."""
    region_info = get_region_info(provider="onedrive", region="eur")
    
    assert region_info["location"] == "Europe"
    assert region_info["country"] == "European Union"
    assert region_info["flag"] == "🇪🇺"
    assert region_info["latitude"] == 50.8503
    assert region_info["longitude"] == 4.3517
    assert region_info["raw"] == "eur"

def test_onedrive_case_insensitive():
    """Test that region lookup is case-insensitive."""
    region_info = get_region_info(provider="onedrive", region="GBR")
    assert region_info["location"] == "United Kingdom"
    assert region_info["country"] == "United Kingdom"

def test_unknown_onedrive_region():
    """Test handling of unknown regions."""
    region_info = get_region_info(provider="onedrive", region="invalid-region")
    assert region_info["location"] == "Unknown"
    assert region_info["country"] == "Unknown"
    assert region_info["raw"] == "invalid-region"
    assert region_info["flag"] is None
    assert region_info["latitude"] is None
    assert region_info["longitude"] is None

def test_onedrive_major_regions():
    """Test major OneDrive regions."""
    regions = {
        "nam": ("North America", "United States", "🇺🇸"),
        "eur": ("Europe", "European Union", "🇪🇺"),
        "gbr": ("United Kingdom", "United Kingdom", "🇬🇧"),
        "apac": ("Asia Pacific", "Singapore", "🇸🇬")
    }
    
    for region, (location, country, flag) in regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["location"] == location
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_onedrive_european_regions():
    """Test European OneDrive regions."""
    regions = {
        "fra": ("France", "France", "🇫🇷"),
        "deu": ("Germany", "Germany", "🇩🇪"),
        "nor": ("Norway", "Norway", "🇳🇴"),
        "che": ("Switzerland", "Switzerland", "🇨🇭")
    }
    
    for region, (location, country, flag) in regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["location"] == location
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_onedrive_asia_pacific():
    """Test Asia Pacific OneDrive regions."""
    regions = {
        "jpn": ("Japan", "Japan", "🇯🇵"),
        "kor": ("South Korea", "South Korea", "🇰🇷"),
        "ind": ("India", "India", "🇮🇳")
    }
    
    for region, (location, country, flag) in regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["location"] == location
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_onedrive_iso_and_country_names():
    """Test that both ISO codes and country names work."""
    # Test ISO codes
    iso_regions = {
        "usa": "United States",
        "gbr": "United Kingdom",
        "deu": "Germany",
        "jpn": "Japan",
        "are": "United Arab Emirates"
    }
    
    for region, country in iso_regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["country"] == country

    # Test country names
    name_regions = {
        "united-states": "United States",
        "united-kingdom": "United Kingdom",
        "germany": "Germany",
        "japan": "Japan",
        "uae": "United Arab Emirates"
    }
    
    for region, country in name_regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["country"] == country

def test_onedrive_oceania_regions():
    """Test Oceania OneDrive regions."""
    regions = {
        "aus": ("Australia", "Australia", "🇦🇺"),
        "nzl": ("New Zealand", "New Zealand", "🇳🇿")
    }
    
    for region, (location, country, flag) in regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["location"] == location
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_onedrive_additional_european_regions():
    """Test additional European OneDrive regions."""
    regions = {
        "prt": ("Portugal", "Portugal", "🇵🇹"),
        "irl": ("Ireland", "Ireland", "🇮🇪")
    }
    
    for region, (location, country, flag) in regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["location"] == location
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_onedrive_middle_east_regions():
    """Test Middle East OneDrive regions."""
    regions = {
        "isr": ("Israel", "Israel", "🇮🇱"),
        "qat": ("Qatar", "Qatar", "🇶🇦")
    }
    
    for region, (location, country, flag) in regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["location"] == location
        assert region_info["country"] == country
        assert region_info["flag"] == flag

def test_onedrive_americas():
    """Test Americas OneDrive regions."""
    regions = {
        "bra": ("Brazil", "Brazil", "🇧🇷")
    }
    
    for region, (location, country, flag) in regions.items():
        region_info = get_region_info(provider="onedrive", region=region)
        assert region_info["location"] == location
        assert region_info["country"] == country
        assert region_info["flag"] == flag 