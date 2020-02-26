from tests.fixtures.address_fixture import *

class BadRequestError(ValueError):
    pass


class AddressBar:
    def convert_address(self, address: str) -> str:
        """
        Convert a URL-like address into a variable name.

        :param address: Address to convert
        :return: variable name
        """
        dot = '.'
        underscore = '_'

        if address == 'exit':
            exit(0)

        if dot in address:
            address = address.replace(dot, underscore)
        else:
            raise BadRequestError

        return address

    def go(self, address: str) -> str:
        """
        Displays page content to the user.

        :param address: Address to go to
        :return: Page content
        """

        try:
            if not self.validate(address) and "_" in address:
                response = globals()[address]
            else:
                url = self.convert_address(address)
                response = globals()[url]
        except KeyError:
            response = 'Error 404 Not Found'
        except BadRequestError:
            response = 'Error 400 Bad Request'

        return response

    def validate(self, url: str) -> bool:
        """
        Validate a URL.

        Right now this means checking if the URL has at least one dot in it.
        :param url: URL to check
        :return: True if valid, else False
        """
        return '.' in url
