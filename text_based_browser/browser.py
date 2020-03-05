from pathlib import Path
from typing import List

from text_based_browser.argument_parser import ArgumentParser


class Browser(object):
    def __init__(self, args: List[str] = []):
        """
        A new Browser object.
        """
        from text_based_browser.resolver import Resolver

        self.argument_parser = ArgumentParser()
        self._args = args
        self.arguments = None
        self.resolver = Resolver(self)
        self.tab_directory = None
        self.url = ''
        self.exit_command = 'exit'

        self.process_arguments()

    def process_arguments(self):
        """
        Process arguments passed to the class instance.

        :return: None
        """
        self.arguments = self.argument_parser.parse_args(self._args)
        self.tab_directory = self.arguments.tab_directory

    def start(self):
        """
        Start the browser.

        This should run an infinite loop until the browser is quit.
        :return:
        """

        if self.tab_directory is not None:
            Path(self.tab_directory).mkdir(exist_ok=True, parents=True)

        while True:
            self.url = input('> ')
            if self.url == self.exit_command:
                self.quit()
            else:
                page_content = self.load_page(self.url)

                print(page_content)

            self.url = ''

    def load_page(self, url: str) -> str:
        """
        Load the page found at the given URL.

        :param url: URL to load
        :return: Page content if the page exists, else error message
        """
        return self.resolver.load_page(url)

    def quit(self, error_code: int = 0):
        """
        Quit the browser with the given error code.

        :param error_code: Error code to use.  Defaults to 0 (No error)
        :return: Error code
        """
        exit(error_code)
