from dataclasses import dataclass, field
from typing import List

@dataclass
class AssetInstanceInformation:
    ip_addresses: List[str] = field(default_factory=list)
    mac_addresses: List[str] = field(default_factory=list)
