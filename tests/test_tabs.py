import shutil
from pathlib import Path

import pytest

from tests.fixtures.address_fixture import nytimes_com
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

    browser_with_absolute_tab_directory.start()

    assert TAB_DIRECTORY.exists() is True


def test_browser_does_not_create_directory_if_none_provided(monkeypatch):
    pytest_add_input(monkeypatch, 'exit')
    browser = Browser()

    browser.start()

    assert TAB_DIRECTORY.exists() is False


def test_tab_not_saved_if_url_is_invalid(monkeypatch, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, '-nytimes.com', 'exit')

    browser_with_absolute_tab_directory.start()

    file = TAB_DIRECTORY / 'nytimes.browsertab'

    assert file.exists() is False


def test_tab_saved_if_url_valid(monkeypatch, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, 'nytimes.com', 'exit')

    browser_with_absolute_tab_directory.start()

    file = TAB_DIRECTORY / 'nytimes'

    assert file.exists() is True


def test_tab_saved_if_url_has_multiple_dots_in_hostname(monkeypatch, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, 'en.wikipedia.org', 'exit')

    browser_with_absolute_tab_directory.start()

    file = TAB_DIRECTORY / 'en.wikipedia'

    assert file.exists() is True


def test_load_tab_from_file_by_providing_hostname_without_extnesion(monkeypatch, capfd, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, 'nytimes.com', 'nytimes', 'exit')

    browser_with_absolute_tab_directory.start()

    file = TAB_DIRECTORY / 'nytimes'

    captured = capfd.readouterr()

    first_page: str = captured.out
    first_page = first_page.strip('> ').strip(str(file)).strip().strip('> Error 404 Page Not Found')

    first_fixture: str = nytimes_com
    first_fixture = first_fixture.strip()
    first_fixture = f"{first_fixture}\n\n\n> \n{first_fixture}"

    assert first_page == first_fixture


def test_do_not_load_tab_from_file_if_not_saved_first(monkeypatch, capfd, browser_with_absolute_tab_directory):
    pytest_add_input(monkeypatch, 'nytimes', 'exit')

    browser_with_absolute_tab_directory.start()

    captured = capfd.readouterr()

    page: str = captured.out
    page = page.strip("> ").strip()

    assert page == "Error 404 Page Not Found"
