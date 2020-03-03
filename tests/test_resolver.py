import pytest

from tests.fixtures.address_fixture import nytimes_com, bloomberg_com
from tests.helpers.input_helper import pytest_add_input
from text_based_browser.browser import Browser
from text_based_browser.resolver import Resolver


ERROR_400 = "Error 400 Bad Request"
ERROR_404 = "Error 404 Page Not Found"


@pytest.fixture()
def resolver():
    browser = Browser()
    resolver = Resolver(browser)

    yield resolver


def test_resolver_converts_addresses(monkeypatch, resolver):
    pytest_add_input(monkeypatch, 'nytimes.com', 'bloomberg.com')

    expected = ['nytimes_com', 'bloomberg_com']

    for variable in expected:
        assert resolver.url_to_variable(input()) == [variable, 'offline']


def test_resolver_returns_400_if_invalid_url(monkeypatch, resolver):
    pytest_add_input(monkeypatch, 'nytimes com', '-bloomberg.com', 'yahoo.com-')

    assert resolver.load_page(input()) == ERROR_400
    assert resolver.load_page(input()) == ERROR_400
    assert resolver.load_page(input()) == ERROR_400


def test_resolver_loads_offline_page(monkeypatch, resolver):
    pytest_add_input(monkeypatch, 'nytimes.com', 'bloomberg.com')

    assert resolver.load_page(input()) == nytimes_com
    assert resolver.load_page(input()) == bloomberg_com


def test_resolver_returns_404_if_offline_page_not_found(monkeypatch, resolver):
    pytest_add_input(monkeypatch, 'yahoo.com')

    assert resolver.load_page(input()) == ERROR_404
