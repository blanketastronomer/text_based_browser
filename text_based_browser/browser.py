from pathlib import Path
from typing import List

from text_based_browser.argument_parser import ArgumentParser


class Browser(object):
    def __init__(self, args: List[str] = []):
        """
        A new Browser object.
        """
        self.argument_parser = ArgumentParser()
        self._args = args
        self.arguments = None
        self.tab_directory = None
        self.url = ''
        self.exit_command = 'exit'

    def start(self):
        """
        Start the browser.

        This should run an infinite loop until the browser is quit.
        :return:
        """
        while True:
            self.url = input('> ')
            if self.url == self.exit_command:
                self.quit()

    def quit(self, error_code: int = 0):
        """
        Quit the browser with the given error code.

        :param error_code: Error code to use.  Defaults to 0 (No error)
        :return: Error code
        """
        exit(error_code)
