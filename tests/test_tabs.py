from pathlib import Path

import pytest

from tests.helpers.input_helper import compatible_input, SYS_STDIN
from text_based_browser.browser import Browser

TEST_DIRECTORY = Path(__file__).parent
DIRECTORY = 'delete_this_directory'
TAB_DIRECTORY = TEST_DIRECTORY / DIRECTORY


@pytest.fixture()
def browser():
    browser = Browser()

    yield browser


def test_browser_creates_tab_directory(monkeypatch, browser):
    args = [
        DIRECTORY
    ]

    current_input = compatible_input('exit')

    monkeypatch.setattr(SYS_STDIN, current_input)

    with pytest.raises(SystemExit):
        browser.start(args)

    assert TAB_DIRECTORY.exists() is True

    TAB_DIRECTORY.rmdir()
