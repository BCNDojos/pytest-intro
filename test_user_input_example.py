from user_input_example import salute, print_salute

def mock_input(message):
    return 'Mark'

def test_user_input(monkeypatch, capsys):
    monkeypatch.setitem(__builtins__, 'input', mock_input)
    message = salute()
    assert message == "Hello, Mark"
    print_salute()
    out, err = capsys.readouterr()
    assert out == "Hello, Mark\n"