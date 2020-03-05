import pytest

from tests.fixtures.address_fixture import nytimes_com, bloomberg_com
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


def test_browser_loads_offline_page(monkeypatch, capfd, browser):
    pytest_add_input(monkeypatch, 'nytimes.com', 'bloomberg.com', 'exit')

    with pytest.raises(SystemExit):
        browser.start()

    captured = capfd.readouterr()

    first_message: str = captured.out
    first_fizture: str = nytimes_com
    second_fixture: str = bloomberg_com

    first_message = first_message.strip('> ').strip()
    first_fizture = first_fizture.strip().strip('> ')
    second_fixture = second_fixture.strip()
    all_fixtures = f"{first_fizture}\n\n\n> \n{second_fixture}"

    assert first_message == all_fixtures
