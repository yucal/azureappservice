import requests
from typing import Optional
class fundabase():
    def __init__(self):
        self.name = "funda"
        self.status = "active"
        self.detail = "Funda service is operational."   
    def access_funda_api(self) -> Optional[dict]:
        base_url = "https://api.funda.nl"
        url = f"{base_url}"
        headers = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.status_code
        except requests.RequestException as e:
            print(f"Error accessing Funda API: {e}")
            return None
    