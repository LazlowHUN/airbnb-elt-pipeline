import requests
import logging
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class WebScraper:
    def __init__(self):
        self.session = self._get_session()

    def _get_session(self):
        session = requests.Session()

        retries = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[502, 503, 504]
        )

        session.mount("https://", HTTPAdapter(max_retries=retries))
        session.mount("http://", HTTPAdapter(max_retries=retries))

        return session

    def get_page_content(self, page_url):
        try:
            response = self.session.get(page_url, timeout=10)
            response.raise_for_status()

            content = response.content
            soup = BeautifulSoup(content, features='html.parser')

            return soup
        
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred while downloading {page_url}: {e}")