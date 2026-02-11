from dataclasses import dataclass
from typing import Optional


@dataclass
class CVSS:
    version: Optional[str] = None
    vector: Optional[str] = None
    base_score: Optional[float] = None
    source: Optional[str] = None
    type: Optional[str] = None
