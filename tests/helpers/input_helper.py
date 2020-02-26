from io import StringIO

SYS_STDIN = 'sys.stdin'


def compatible_input(*inputs) -> StringIO:
    """
    Render a list of inputs into something that pytest's "monkeypatch" can use.

    :param inputs: Inputs to send to stdin
    :return: Something "monkeypatch" can use
    """
    return StringIO("\n".join(inputs))
