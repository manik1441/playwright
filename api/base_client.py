import requests
from config.utils.logger import get_logger

class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = get_logger("API_Client")

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET Request to: {url}")
        response = requests.get(url, params=params)
        return response