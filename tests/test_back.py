import pytest

from tests.helpers.input_helper import pytest_add_input
from text_based_browser.browser import Browser


@pytest.fixture()
def browser():
    browser = Browser()

    yield browser


def test_browser_responds_to_back_command(monkeypatch, capfd, browser):
    pytest_add_input(monkeypatch, 'bloomberg.com', 'nytimes.com', 'back', 'exit')

    browser.start()

    captured = capfd.readouterr()

    pages = captured.out.split('> ')
    true_pages = []

    for i in range(0, len(pages)):
        if pages[i] != '':
            true_pages.append(pages[i].strip())

    print()
    for i in range(0, len(true_pages)):
        print(f"Page {i}: {repr(true_pages[i])}")

    assert true_pages[2] == true_pages[1]
