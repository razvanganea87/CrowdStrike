from dataclasses import dataclass
from typing import Optional
from enum import Enum


class ComponentType(Enum):
    APPLICATION = 1
    CONTAINER = 2
    CRYPTOGRAPHIC_ASSET = 3
    DATA = 4
    DEVICE = 5
    DEVICE_DRIVER = 6
    FILE = 7
    FIRMWARE = 8
    FRAMEWORK = 9
    LIBRARY = 10
    MACHINE_LEARNING_MODEL = 11
    OPERATING_SYSTEM = 12
    PLATFORM = 13


@dataclass
class Component:
    type: ComponentType
    product: Optional[str] = None
    vendor: Optional[str] = None
    version: Optional[str] = None
    display_name: Optional[str] = None
