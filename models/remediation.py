from dataclasses import dataclass
from typing import Optional


@dataclass
class Remediation:
    suggestion: Optional[str] = None
    source: Optional[str] = None
    fixed_in_version: Optional[str] = None
