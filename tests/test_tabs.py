import shutil
from pathlib import Path

import pytest

from tests.helpers.input_helper import pytest_add_input
from text_based_browser.browser import Browser

DIRECTORY = 'delete_this_directory'
TEST_DIRECTORY = Path(__file__).parent
TAB_DIRECTORY = TEST_DIRECTORY / DIRECTORY


def remove_tab_directory(directory: Path):
    """
    Remove the user-supplied tab directory.

    :param directory: Directory to remove.
    :return: None
    """
    if directory.exists():
        shutil.rmtree(directory)


@pytest.fixture()
def browser_with_relative_tab_directory():
    browser = Browser([DIRECTORY])

    yield browser

    remove_tab_directory(TAB_DIRECTORY)


@pytest.fixture()
def browser_with_absolute_tab_directory():
    browser = Browser([str(TAB_DIRECTORY)])

    yield browser

    remove_tab_directory(TAB_DIRECTORY)


def test_browser_creates_tab_directory(monkeypatch, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, 'exit')

    with pytest.raises(SystemExit):
        browser_with_absolute_tab_directory.start()

    assert TAB_DIRECTORY.exists() is True


def test_browser_does_not_create_directory_if_none_provided(monkeypatch):
    pytest_add_input(monkeypatch, 'exit')
    browser = Browser()

    with pytest.raises(SystemExit):
        browser.start()

    assert TAB_DIRECTORY.exists() is False


def test_tab_not_saved_if_url_is_invalid(monkeypatch, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, '-nytimes.com', 'exit')

    with pytest.raises(SystemExit):
        browser_with_absolute_tab_directory.start()

    file = TAB_DIRECTORY / 'nytimes.browsertab'

    assert file.exists() is False


def test_tab_saved_if_url_valid(monkeypatch, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, 'nytimes.com', 'exit')

    with pytest.raises(SystemExit):
        browser_with_absolute_tab_directory.start()

    file = TAB_DIRECTORY / 'nytimes.browsertab'

    assert file.exists() is True


def test_tab_saved_if_url_has_multiple_dots_in_hostname(monkeypatch, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, 'en.wikipedia.org', 'exit')

    with pytest.raises(SystemExit):
        browser_with_absolute_tab_directory.start()

    file = TAB_DIRECTORY / 'en.wikipedia.browsertab'

    assert file.exists() is True
