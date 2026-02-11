import requests
from config import Config
from crowd_strike_auth_error import CrowdStrikeAuthError
from typing import List, Dict

class CrowdStrikeClient:
    def __init__(self):
        self.config = Config()
        self.access_token = None

    def authenticate(self) -> str:
        url = f"{self.config.base_url}/oauth2/token"

        data = {
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret
        }

        try:
            response = requests.post(url, data=data, timeout=30)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            response = error.response
            raise CrowdStrikeAuthError(
                f"Authentication failed with status {response.status_code}: {response.text}"
            ) from error
        except requests.exceptions.RequestException as error:
            raise CrowdStrikeAuthError(
                f"Error connecting to CrowdStrike OAuth endpoint: {str(error)}"
            ) from error

        payload = response.json()
        self.access_token = payload.get("access_token")

        if not self.access_token:
            raise CrowdStrikeAuthError("Authentication response did not contain access_token")

        return self.access_token

    def fetch_asset_ids(self, limit=100)  -> List[str]:
        path = "/devices/queries/devices/v1"
        params = {
            "limit": limit
        }

        response = self._get(path, params)
        return response.get("resources", [])

    def fetch_assets(self, limit=100) -> List[Dict]:
        asset_ids = self.fetch_asset_ids(limit)

        if not asset_ids:
            return []

        path = "/devices/entities/devices/v2"
        params = {
            "ids": asset_ids
        }

        response = self._get(path, params)
        return response.get("resources", [])

    def fetch_vulnerabilities(self) -> List[Dict]:
        path = "/spotlight/combined/vulnerabilities/v1"

        all_vulnerabilities: List[Dict] = []
        limit = 1000
        offset = 0

        step = 0

        while True:
            if step >= 3:
                break

            step += 1

            params = {
                "filter": "status:'open'",
                "limit": limit,
                "offset": offset
            }

            response = self._get(path, params)
            vulnerabilities = response.get("resources", [])

            if not vulnerabilities:
                break

            all_vulnerabilities.extend(vulnerabilities)

            if len(vulnerabilities) < limit:
                break

            offset += limit

        return all_vulnerabilities

    def _get_headers(self) -> Dict[str, str]:
        if not self.access_token:
            self.authenticate()

        return {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json"
        }

    def _get(self, path, params=None) -> Dict:
        url = f"{self.config.base_url}{path}"
        headers = self._get_headers()

        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=30
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            resp = error.response
            raise Exception(
                f"GET {path} failed (HTTP {resp.status_code}): {resp.text}"
            )
        except requests.exceptions.RequestException as error:
            raise Exception(
                f"Error connecting to CrowdStrike API: {str(error)}"
            )

        return response.json()