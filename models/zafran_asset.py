from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime

from models.asset_instance_information import AssetInstanceInformation
from models.instance_identifier import InstanceIdentifier
from models.instance_property_value import InstancePropertyValue
from models.instance_type import InstanceType


@dataclass
class ZafranAsset:
    instance_id: str
    name: str
    asset_information: AssetInstanceInformation
    operating_system: str
    identifiers: List[InstanceIdentifier] = field(default_factory=list)
    instance_properties: Dict[str, InstancePropertyValue] = field(default_factory=dict)
    inet_evidence: Optional[dict] = None
    source_last_seen: Optional[datetime] = None
    sbom_components: List[dict] = field(default_factory=list)
    labels: List[dict] = field(default_factory=list)
    key_value_tags: List[dict] = field(default_factory=list)
    instance_type: Optional[InstanceType] = None
