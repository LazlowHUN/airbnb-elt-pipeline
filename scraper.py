import requests
import logging
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

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

        return session