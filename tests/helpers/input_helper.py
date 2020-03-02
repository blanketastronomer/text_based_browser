from io import StringIO

SYS_STDIN = 'sys.stdin'


def compatible_input(*inputs) -> StringIO:
    """
    Render a list of inputs into something that pytest's "monkeypatch" can use.

    :param inputs: Inputs to send to stdin
    :return: Something "monkeypatch" can use
    """
    return StringIO("\n".join(inputs))


def pytest_add_input(pytest_monkeypatch_object, *values: str):
    """
    Allow data to be passed to STDIN in a pytest test environment.

    Relies on pytest's "monkeypatch" feature.

    :param pytest_monkeypatch_object: Pytest monkeypatch object
    :param values: Values to pass STDIN
    :return: None
    """
    current_input = compatible_input(*values)

    pytest_monkeypatch_object.setattr(SYS_STDIN, current_input)
