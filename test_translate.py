from functions import translate

def test_translate(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "french")
    assert translate() == 0
    
def test_langauge_not_supported(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "error")
    assert translate() == 1
    