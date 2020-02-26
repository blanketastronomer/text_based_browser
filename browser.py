import sys

from text_based_browser.browser import Browser

if __name__ == '__main__':
    browser = Browser()

    browser.start(sys.argv[1:])
