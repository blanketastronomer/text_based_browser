import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse_args(self, args):
        self.parser.add_argument('tab_directory', default=None, help="Directory where tab files are stored.", nargs='?')

        return self.parser.parse_args(args)
