from cloud_regions_info import get_region_info

def test_alibaba_china_regions():
    """Test multiple regions in China."""
    regions = {
        "cn-hangzhou": "Hangzhou",
        "cn-shanghai": "Shanghai",
        "cn-beijing": "Beijing",
        "cn-shenzhen": "Shenzhen",
        "cn-guangzhou": "Guangzhou",
        "cn-qingdao": "Qingdao",
        "cn-chengdu": "Chengdu",
        "cn-wulanchabu": "Ulanqab"
    }
    
    for region, city in regions.items():
        region_info = get_region_info(provider="alibaba", region=region)
        assert region_info["country"] == "China"
        assert region_info["location"] == city
        assert region_info["flag"] == "🇨🇳"

def test_alibaba_southeast_asia():
    """Test Southeast Asia regions."""
    regions = {
        "ap-southeast-1": ("Singapore", "Singapore", "🇸🇬"),
        "ap-southeast-3": ("Kuala Lumpur", "Malaysia", "🇲🇾"),
        "ap-southeast-5": ("Jakarta", "Indonesia", "🇮🇩"),
        "ap-southeast-6": ("Manila", "Philippines", "🇵🇭"),
        "ap-southeast-7": ("Bangkok", "Thailand", "🇹🇭")
    }
    
    for region, (city, country, flag) in regions.items():
        region_info = get_region_info(provider="alibaba", region=region)
        assert region_info["location"] == city
        assert region_info["country"] == country
        assert region_info["flag"] == flag 