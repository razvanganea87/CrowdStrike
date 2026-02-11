from dataclasses import dataclass
from typing import Optional

@dataclass
class InstancePropertyValue:
    string_value: Optional[str] = None
    int_value: Optional[int] = None
    bool_value: Optional[bool] = None
