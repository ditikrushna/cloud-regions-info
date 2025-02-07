# Cloud Regions Info

A Python package that provides detailed information about cloud regions across different cloud providers.

[![PyPI version](https://badge.fury.io/py/cloud-regions-info.svg)](https://badge.fury.io/py/cloud-regions-info)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- Get detailed information about cloud regions
- Currently supports:
  - AWS (full support)
  - Azure (placeholder)
  - GCP (placeholder)
- Region information includes:
  - Region name and code
  - Geographic location
  - Availability zones
  - Service availability

## Installation

Install using pip:
```bash
pip install cloud-regions-info
```

Or with Poetry:
```bash
poetry add cloud-regions-info
```

## Usage

```python
from cloud_regions_info import get_region_info

# Get AWS region info
region_info = get_region_info("us-east-1", provider="aws")
print(region_info.name)  # US East (N. Virginia)
print(region_info.code)  # us-east-1
print(region_info.location)  # Northern Virginia

# Check if a service is available in a region
is_available = region_info.has_service("ec2")
```

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cloud-regions-info.git
cd cloud-regions-info
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Run tests:
```bash
poetry run pytest
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests (`poetry run pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Areas for Contribution

- Expanding Azure and GCP support
- Adding more region information
- Improving documentation
- Adding new cloud providers
- Bug fixes and improvements

## Data Sources

The region information is sourced from:
- AWS: Official AWS documentation and APIs
- Azure: (Placeholder for future implementation)
- GCP: (Placeholder for future implementation)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who help maintain and improve this package
- Cloud provider documentation and APIs that make this possible

## Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/yourusername/cloud-regions-info/issues) page
2. Create a new issue if your problem isn't already listed

## Project Status

### Cloud Providers
| Provider | Status | Implementation |
|----------|--------|----------------|
| AWS      | ✅     | Complete       |
| Azure    | 🚧     | In Progress    |
| GCP      | 🚧     | Planned        |
| Oracle Cloud | 📅  | Planned       |
| DigitalOcean | 📅  | Planned       |
| IBM Cloud    | 📅  | Planned       |
| Alibaba Cloud| 📅  | Planned       |

### SaaS Applications
| Application | Status | Implementation |
|-------------|--------|----------------|
| Microsoft 365 | 📅   | Planned        |
| - SharePoint  | 📅   | Planned        |
| - OneDrive   | 📅   | Planned        |
| - Teams      | 📅   | Planned        |
| Atlassian    | 📅   | Planned        |
| - Jira       | 📅   | Planned        |
| - Confluence | 📅   | Planned        |
| Salesforce   | 📅   | Planned        |
| ServiceNow   | 📅   | Planned        |
| Workday      | 📅   | Planned        |

Status Legend:
- ✅ Complete
- 🚧 In Progress
- 📅 Planned
- ❌ Not Started

## Roadmap

- [ ] Complete Azure regions implementation
- [ ] Add GCP regions support
- [ ] Add major cloud providers (Oracle, DigitalOcean, IBM)
- [ ] Implement Microsoft 365 services regional mapping
- [ ] Add Atlassian services regional deployment info
- [ ] Implement region comparison functionality
- [ ] Add service availability matrix
- [ ] Create detailed documentation site
- [ ] Add region cost information
- [ ] Implement caching mechanism

---

Made with ❤️ by [Ditikrushna Giri](https://ditikrushna.xyz/)
