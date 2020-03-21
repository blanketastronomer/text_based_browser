from pathlib import Path
from typing import List, Union

from text_based_browser.argument_parser import ArgumentParser
from text_based_browser.history import History


class Browser(object):
    def __init__(self, args: List[str] = []):
        """
        A new Browser object.
        :param args: Arguments passed via the commandline
        """
        from text_based_browser.resolver import Resolver

        self._args = args
        self.argument_parser = ArgumentParser()
        self.back_command = 'back'
        self.exit_command = 'exit'
        self.history = History()
        self.resolver = Resolver(self)
        self.url = None

        self.process_arguments()

    def process_arguments(self):
        """
        Process arguments passed to the class instance.
        """
        self.arguments = self.argument_parser.parse_args(self._args)
        self.tab_directory = self.arguments.tab_directory

    def start(self):
        """
        Start the browser.

        This should run an infinite loop until the browser is quit.
        """

        try:
            if self.tab_directory is not None:
                Path(self.tab_directory).mkdir(exist_ok=True, parents=True)

            while True:
                self.url = input('> ')
                if self.url == self.exit_command:
                    self.quit()
                else:
                    if self.url == self.back_command:
                        page_url = self.history.pop()
                        page_content = self.load_page(page_url)
                    else:
                        page_url = self.url
                        page_content = self.load_page(page_url)
                        self.history.push(self.url)

                    print(page_content)

                    self.save_page(page_url, page_content)
        except SystemExit:
            pass

    def load_page(self, url: str) -> str:
        """
        Load the page found at the given URL.

        :param url: URL to load
        :return: Page content if the page exists, else error message
        """
        if self.page_saved(url):
            return self.load_page_from_file(url)
        else:
            return self.resolver.load_page(url)

    def save_page(self, url: str, page_content: str):
        """
        Save a page with the given URL and content to the tab directory if it exists.

        :param url: Page URL
        :param page_content: Page content
        """
        save_file = self.get_tab_file_path(url)

        try:
            with open(save_file, 'w') as f:
                f.write(page_content)
        except TypeError:
            pass

    def page_saved(self, url: str) -> bool:
        """
        Check if a page corresponding to the given URL has been saved to disk.

        :param url: URL to derive the filename from
        :return: True if page was saved to disk, else False
        """
        try:
            if url != self.exit_command:
                file = self.get_tab_file_path(url)

                return Path(file).exists()
        except TypeError:
            return False

    def quit(self, error_code: int = 0):
        """
        Quit the browser with the given error code.

        :param error_code: Error code to use.  Defaults to 0 (NO ERROR)
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

        try:
            # self.tab_directory exists
            if len(parts) > 1:
                # Multiple parts, such as "en.wikipedia.org"
                split = parts[:len(parts) - 1]
            else:
                # Single part, such as "reddit.com"
                split = parts

            filename = '.'.join(split)

            save_file = Path(self.tab_directory) / filename

            return save_file
        except TypeError:
            pass

    def load_page_from_file(self, url: str) -> str:
        """
        Load the page corresponding to the given URL from disk.

        :param url: Page URL
        :return: Page content
        """
        file_to_load = self.get_tab_file_path(url)
        page_content: str = None

        try:
            with open(file_to_load, 'r') as f:
                page_content = f.read()
        except TypeError:
            pass

        return page_content
