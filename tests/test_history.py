import pytest

from tests.helpers.input_helper import pytest_add_input
from text_based_browser.browser import Browser
from text_based_browser.history import History


@pytest.fixture()
def browser():
    browser = Browser()

    yield browser


def test_browser_has_a_history_stack(monkeypatch, browser):
    pytest_add_input(monkeypatch, 'exit')

    browser.start()

    assert type(browser.history) == History


def test_browser_history_stack_is_empty_on_boot(monkeypatch, browser):
    pytest_add_input(monkeypatch, 'exit')

    browser.start()

    assert browser.history.empty() is True


def test_browser_history_stack_adds_pages(monkeypatch, browser):
    pytest_add_input(monkeypatch, 'nytimes.com', 'bloomberg.com', 'exit')

    browser.start()

    assert browser.history.empty() is False
    assert len(browser.history) == 2
    assert browser.history.peek() == 'bloomberg.com'
    assert browser.history.pop() == 'bloomberg.com'