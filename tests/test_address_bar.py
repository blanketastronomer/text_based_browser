import pytest

from tests.fixtures.address_fixture import nytimes_com, bloomberg_com
from tests.helpers.input_helper import compatible_input, SYS_STDIN
from text_based_browser.address_bar import AddressBar


@pytest.fixture()
def address_bar():
    address_bar = AddressBar()

    yield address_bar


def test_address_bar_converts_addresses(monkeypatch, address_bar):
    current_input = compatible_input('nytimes.com', 'bloomberg.com')

    monkeypatch.setattr(SYS_STDIN, current_input)

    assert address_bar.convert_address(input()) == 'nytimes_com'
    assert address_bar.convert_address(input()) == 'bloomberg_com'


# @pytest.mark.skip()
def test_address_bar_processes_exit_command(monkeypatch, address_bar):
    current_input = compatible_input('exit')

    monkeypatch.setattr('sys.stdin', current_input)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        address_bar.convert_address(input())

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_address_bar_loads_page(monkeypatch, address_bar):
    current_input = compatible_input('nytimes.com', 'bloomberg.com')

    monkeypatch.setattr(SYS_STDIN, current_input)

    assert address_bar.go(input()) == nytimes_com
    assert address_bar.go(input()) == bloomberg_com


def test_address_bar_shows_404_error_if_address_not_found(monkeypatch, address_bar):
    current_input = compatible_input('nytimes.org')

    monkeypatch.setattr(SYS_STDIN, current_input)

    assert address_bar.go(input()) == 'Error 404 Not Found'


def test_address_bar_shows_400_if_invalid_url(monkeypatch, address_bar):
    current_input = compatible_input('nytimes^org')

    monkeypatch.setattr(SYS_STDIN, current_input)

    assert address_bar.go(input()) == 'Error 400 Bad Request'
