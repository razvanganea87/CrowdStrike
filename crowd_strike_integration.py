from crowd_strike_client import CrowdStrikeClient
from mappers.asset_mapper import AssetMapper
from mappers.vulnerability_mapper import VulnerabilityMapper

class CrowdStrikeIntegration:
    def __init__(self):
        self.client = CrowdStrikeClient()

    def run(self):
        raw_assets = self.client.fetch_assets()
        raw_vulnerabilities = self.client.fetch_vulnerabilities()

        zafran_assets = AssetMapper.map(raw_assets)
        zafran_vulnerabilities = VulnerabilityMapper.map(
            raw_vulnerabilities,
            zafran_assets
        )

        return zafran_assets, zafran_vulnerabilities
