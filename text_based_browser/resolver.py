import re
from typing import List
from urllib.parse import urlparse, urlunparse

from tests.fixtures.address_fixture import *
from text_based_browser.browser import Browser

ERROR_BAD_REQUEST = "Error 400 Bad Request"
ERROR_PAGE_NOT_FOUND = "Error 404 Page Not Found"


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

    def load_page(self, url: str) -> str:
        """
        Load a webpage found at the given URL.

        NOTE: At the moment, this DOES NOT actually call out to the Internet.

        :param url: URL of the webpage to load.
        :return:
        """
        response = ''

        if self.valid_hostname(url):
            url_to_load, status = self.url_to_variable(url)
            response = ''

            try:
                if status == 'offline':
                    response = globals()[url_to_load]
            except KeyError:
                response = ERROR_PAGE_NOT_FOUND
        else:
            response = ERROR_BAD_REQUEST

        return response

    def valid_hostname(self, hostname: str) -> bool:
        """
        Check if the given hostname is valid under RFC 1123.

        :param hostname: Hostname to validate
        :return: True if valid, else False
        """
        invalid_pattern = re.compile(r"-*[^a-zA-Z\.]+-*", re.IGNORECASE)

        searched = invalid_pattern.search(hostname)

        if searched:
            return False
        else:
            return True
