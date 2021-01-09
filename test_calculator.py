import pytest
import yaml
from pythoncode.calculator import Calculator
from get_datas import get_datas


class TestCalc:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("关闭计算")

    def setup_class(self):
        self.clc = Calculator()

    @pytest.mark.parametrize("a,b,hopevalue",get_datas("add_datas"),ids=get_datas("myids"))
    def test_add(self,a,b,hopevalue):
        #加法测试
        result = self.clc.add(a,b)
        assert result == hopevalue

    @pytest.mark.parametrize("a,b,hopevalue",get_datas("sub_datas"),ids=get_datas("myids"))
    def test_sub(self,a,b,hopevalue):
        #减法测试
        result = self.clc.sub(a,b)
        assert result == hopevalue

    @pytest.mark.parametrize("a,b,hopevalue", get_datas("mul_datas"),
                             ids=get_datas("myids"))
    def test_mul(self, a, b, hopevalue):
        #乘法测试
        result = self.clc.mul(a, b)
        assert result == hopevalue

    @pytest.mark.parametrize("a,b,hopevalue", get_datas("div_datas"),
                             ids=get_datas("myids"))
    def test_div(self, a, b, hopevalue):
        #除法测试
        result = self.clc.div(a, b)
        assert result == hopevalue