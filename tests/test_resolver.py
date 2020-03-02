import pytest

from tests.helpers.input_helper import pytest_add_input
from text_based_browser.browser import Browser
from text_based_browser.resolver import Resolver


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
