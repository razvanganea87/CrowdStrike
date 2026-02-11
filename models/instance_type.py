from enum import Enum

class InstanceType(Enum):
    UNKNOWN = 0
    MACHINE = 1
    CONTAINER_IMAGE = 2
    SERVERLESS = 3
    MOBILE_DEVICE = 4
    NETWORK_DEVICE = 5
    OT_IOT_DEVICE = 6
    DATA_STORE = 7
    CODE_PROJECT = 8
    WEB_APP_API = 9