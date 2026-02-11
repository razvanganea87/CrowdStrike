from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.base_url = os.getenv("CROWDSTRIKE_BASE_URL")
        self.client_id = os.getenv("CROWDSTRIKE_CLIENT_ID")
        self.client_secret = os.getenv("CROWDSTRIKE_CLIENT_SECRET")
        self.page_size = int(os.getenv("CROWDSTRIKE_PAGE_SIZE", 1000))
