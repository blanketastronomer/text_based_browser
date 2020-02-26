from tests.fixtures.address_fixture import *


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
            exit(42)

        if dot in address:
            address = address.replace(dot, underscore)

        return address

    def go(self, address: str) -> str:
        """
        Displays page content to the user.

        :param address: Address to go to
        :return: Page content
        """
        url = self.convert_address(address)

        try:
            response = globals()[url]
        except KeyError:
            response = '404 Not Found'

        return response
