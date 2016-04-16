import sqlite3
from data_example import get_total

class FakeConn():
    def cursor(self):
        return FakeCursor()

class FakeCursor():
    def execute(self, query):
        pass
    
    def fetchall(self):
        return  [
                    ('2006-01-05', 'RHAT', 1.0, 10.0),
                    ('2006-03-28', 'IBM', 1.0, 10.0),
                    ('2006-04-05', 'MSFT', 1.0, 10.0),
                    ('2006-04-06', 'IBM3', 1.0, 10.0)
                ]

def test_get_total(monkeypatch):
    def mock_conn(file_name):
        return FakeConn()
    monkeypatch.setattr(sqlite3, 'connect', mock_conn)
    total = get_total()
    assert total == 40.0