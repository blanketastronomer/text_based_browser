from pathlib import Path
from typing import List

from text_based_browser.address_bar import AddressBar, BadRequestError
from text_based_browser.argument_parser import ArgumentParser


class Browser(object):
    def __init__(self):
        """
        A new Browser object.
        """
        self.argument_parser = ArgumentParser()
        self.arguments = None
        self.address_bar = AddressBar()
        self.tab_directory = None
        self.url = ''
        self.exit_command = 'exit'

    def start(self, args: List[str]):
        """
        Start the browser.

        This should run an infinite loop until the browser is quit.
        :return:
        """
        # Check if a tab directory has been passed to the program as an argument
        self.arguments = self.argument_parser.parse_args(args)
        tab_directory = self.arguments.tab_directory
        self.tab_directory = tab_directory

        if tab_directory is not None:
            Path(tab_directory).mkdir(exist_ok=True)

        while self.url != self.exit_command:
            try:
                self.url = self.address_bar.convert_address(input('> '))
            except BadRequestError:
                pass

            self.render_page(self.url)

            self.url = ''

    def render_page(self, url: str) -> str:
        """
        Renders a page given a URL

        :param url: URL of the page to render
        :return: Page content
        """
        page_content = self.address_bar.go(url)
        print(page_content)

        if self.tab_directory is not None:
            self.save_page(url, page_content)

    def save_page(self, url: str, page_content: str):
        """
        Saves a page as a tab.

        :param url: URL of the page to save
        :param page_content: Page content to save
        :return: Nothing
        """
        components = url.split('_')
        filename = url.split('_')[:len(components) - 1]
        filename = '.'.join(filename)
        filename = f"{filename}.browsertab"

        save_file = Path(self.tab_directory) / filename

        if not save_file.is_absolute():
            save_file = Path.cwd() / save_file

        with open(save_file, 'w') as f:
            f.write(page_content)

    def quit(self, error_code: int = 0):
        """
        Quit the browser with the given error code.

        :param error_code: Error code to use.  Defaults to 0 (No error)
        :return: Error code
        """
        exit(error_code)
