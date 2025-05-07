import pytest


class TestDDT:

    data = [(1,2,3), (5,10,20)]

    @pytest.mark.parametrize("a, b, c", data)
    def test_multi_param(self, a, b, c):
        sum = a + b + c
        print(f"{a} + {b} + {c} = {sum} ")
        assert sum > 20, f"Fail if {sum} <= 20"