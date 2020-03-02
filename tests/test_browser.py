import pytest

from tests.helpers.input_helper import pytest_add_input
from text_based_browser.browser import Browser


@pytest.fixture()
def browser():
    browser = Browser()

    yield browser


def test_browser_responds_to_exit_command(monkeypatch, browser):
    pytest_add_input(monkeypatch, 'exit')

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        browser.start()

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 0


def test_browser_loops_until_exit_command(monkeypatch, browser):
    pytest_add_input(monkeypatch, 'yahoo.com', 'google.com', 'reddit.com', 'exit')

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        browser.start()

    assert pytest_wrapped_error.type == SystemExit
    assert pytest_wrapped_error.value.code == 0
