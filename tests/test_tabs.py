import shutil
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

    shutil.rmtree(TAB_DIRECTORY)


def test_browser_saves_a_tab_in_relative_directory(monkeypatch, browser):
    args = [
        DIRECTORY
    ]

    current_input = compatible_input('nytimes.com', 'exit')

    monkeypatch.setattr(SYS_STDIN, current_input)

    file = TAB_DIRECTORY / 'nytimes.browsertab'

    with pytest.raises(SystemExit):
        browser.start(args)

    assert file.exists() is True

    shutil.rmtree(TAB_DIRECTORY)


def test_browser_saves_a_tab_in_absolute_directory(monkeypatch, browser):
    args = [
        str(TAB_DIRECTORY)
    ]

    current_input = compatible_input('nytimes.com', 'exit')

    monkeypatch.setattr(SYS_STDIN, current_input)

    file = TAB_DIRECTORY / 'nytimes.browsertab'

    with pytest.raises(SystemExit):
        browser.start(args)

    assert file.exists() is True

    shutil.rmtree(TAB_DIRECTORY)


def test_browser_does_not_save_a_tab_if_url_is_invalid(monkeypatch, browser):
    args = [
        str(TAB_DIRECTORY)
    ]

    current_input = compatible_input('nytimes&com', 'exit')

    monkeypatch.setattr(SYS_STDIN, current_input)

    file = TAB_DIRECTORY / 'nytimes.browsertab'

    with pytest.raises(SystemExit):
        browser.start(args)

    assert file.exists() is False

    shutil.rmtree(TAB_DIRECTORY)


def test_browser_saves_tab_with_multiple_dots(monkeypatch, browser):
    args = [
        str(TAB_DIRECTORY)
    ]

    current_input = compatible_input('en.wikipedia.org', 'exit')

    monkeypatch.setattr(SYS_STDIN, current_input)

    file = TAB_DIRECTORY / 'en.wikipedia.browsertab'

    with pytest.raises(SystemExit):
        browser.start(args)

    assert file.exists() is True

    shutil.rmtree(TAB_DIRECTORY)
