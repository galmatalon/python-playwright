class TestDemo:

    def test_01_stam(self):
        a = 10
        b = 10
        assert a == b

    def test_02_stam(self):
        age = 30
        assert age > 40, f"{age} is smaller the 40"
