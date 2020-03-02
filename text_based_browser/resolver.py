from typing import List
from urllib.parse import urlparse, urlunparse

from text_based_browser.browser import Browser


class Resolver:
    def __init__(self, browser: Browser):
        """
        Address resolver class.

        :param browser: Parent Browser instance
        """
        self.browser = browser

    def url_to_variable(self, url: str) -> List[str]:
        """
        Convert a URL into a variable name.

        :param url: URL to convert to variable
        :return: Variable name
        """
        url = urlparse(url)
        status = None

        if url.scheme == '':
            status = 'offline'
            return [
                Resolver.offline_url(urlunparse(url)),
                status
            ]

    @staticmethod
    def offline_url(url: str) -> str:
        """
        Sanitized an offline URL into a variable name for internal processing.

        :param url: URL to sanitize
        :return: Variable name
        """
        return url.replace('.', '_')
