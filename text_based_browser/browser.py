from text_based_browser.address_bar import AddressBar


class Browser(object):
    def __init__(self):
        """
        A new Browser object.
        """
        self.address_bar = AddressBar()
        self.url = ''
        self.exit_command = 'exit'

    def start(self):
        """
        Start the browser.

        This should run an infinite loop until the browser is quit.
        :return:
        """
        while self.url != self.exit_command:
            self.url = self.address_bar.convert_address(input('> '))

            self.render_page(self.url)

            self.url = ''

    def render_page(self, url: str) -> str:
        """
        Renders a page given a URL

        :param url: URL of the page to render
        :return: Page content
        """
        print(self.address_bar.go(url))
