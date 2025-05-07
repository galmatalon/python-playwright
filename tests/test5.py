import pytest
from tests.base_test import BaseTest



class Test2(BaseTest):

    data = [(1,2,3),(-1,-1,-2),(1,5,6),(5,5,8)]

    @pytest.mark.parametrize("a,b,c",data)
    def test_01_wizards(self,a,b,c):
        assert a+b == c






