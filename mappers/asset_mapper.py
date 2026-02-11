from typing import List
from models.zafran_asset import ZafranAsset
from models.asset_instance_information import AssetInstanceInformation
from models.instance_identifier import InstanceIdentifier

class AssetMapper:

    @staticmethod
    def map(assets: List[dict]) -> List[ZafranAsset]:
        instances: List[ZafranAsset] = []

        for asset in assets:
            # --- Identifiers (CROWDSTRIKE_AID)
            identifiers = []
            device_id = asset.get("device_id")
            if device_id:
                identifiers.append(
                    InstanceIdentifier(key="CROWDSTRIKE_AID", value=device_id)
                )

            asset_info = AssetInstanceInformation(
                ip_addresses=asset.get("local_ip", []),
                mac_addresses=asset.get("mac_address", [])
            )

            instance_properties = {
                "device_type": asset.get("device_type", ""),
                "status": asset.get("status", "")
            }

            instance = ZafranAsset(
                instance_id=device_id,
                name=asset.get("hostname", ""),
                asset_information=asset_info,
                operating_system=asset.get("platform_name", ""),
                identifiers=identifiers,
                instance_properties=instance_properties,
                inet_evidence=None,
                source_last_seen=None,
                sbom_components=[],
                labels=[],
                key_value_tags=[],
                instance_type=None
            )

            instances.append(instance)

        return instances
