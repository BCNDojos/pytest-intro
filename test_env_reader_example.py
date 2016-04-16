import os
from env_reader_example import get_user

def test_get_user(monkeypatch):
    monkeypatch.setitem(os.environ, 'USER', 'root')
    user = get_user()
    assert user == "root"