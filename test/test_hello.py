from hello import hello

def test_default():
    assert hello()=="hello , wolrd"

def test_david():
    assert hello("David") == "hello , david"