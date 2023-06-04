from functions import translate

def test_translate(monkeypatch):
    inputs = iter(['french', 'Hi how are you?'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert translate() == 0
    
def test_langauge_not_supported(monkeypatch):
    inputs = iter(['error', 'Hi how are you?'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert translate() == 1
    
def test_number_error(monkeypatch):
    inputs = iter(['chinese', '123'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert translate() == 2