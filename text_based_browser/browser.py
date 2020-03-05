from pathlib import Path
from typing import List, Union

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

                self.save_page(self.url, page_content)

            self.url = ''

    def load_page(self, url: str) -> str:
        """
        Load the page found at the given URL.

        :param url: URL to load
        :return: Page content if the page exists, else error message
        """
        return self.resolver.load_page(url)

    def save_page(self, url: str, page_content: str):
        """
        Save a page with the given URL and content to the tab directory if it exists.

        :param url: Page URL
        :param page_content: Page content
        :return: None
        """
        save_file = self.get_tab_file_path(self.url)

        try:
            with open(save_file, 'w') as f:
                f.write(page_content)
        except TypeError:
            pass

    def quit(self, error_code: int = 0):
        """
        Quit the browser with the given error code.

        :param error_code: Error code to use.  Defaults to 0 (No error)
        :return: Error code
        """
        exit(error_code)

    def get_tab_file_path(self, url: str) -> Union[str, None]:
        """
        Get the path to the tab file for the given URL.

        If the file doesn't exist, it'll return None.

        :param url: URL to derive the file path
        :return: Path as a string if it exists, else None
        """
        parts = url.split('.')
        extension = 'browsertab'

        try:
            # self.tab_directory exists
            if len(parts) > 1:
                # Multiple parts, such as "en.wikipedia.org"
                split = parts[:len(parts) - 1]
            else:
                # Single part, such as "reddit.com"
                split = parts

            split.append(extension)

            filename = '.'.join(split)

            save_file = Path(self.tab_directory) / filename

            return save_file
        except TypeError:
            pass
