"""calculator 模块的 pytest 单元测试。"""

import pytest

from calculator import (
    DivisionByZeroError,
    add,
    divide,
    multiply,
    subtract,
)


# ---------- 正常场景 ----------

class TestAdd:
    def test_integers(self):
        assert add(2, 3) == 5

    def test_negatives(self):
        assert add(-1, -2) == -3

    def test_floats(self):
        assert add(1.5, 2.25) == pytest.approx(3.75)

    def test_zero(self):
        assert add(0, 7) == 7


class TestSubtract:
    def test_integers(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 8) == -5

    def test_floats(self):
        assert subtract(2.5, 1.1) == pytest.approx(1.4)


class TestMultiply:
    def test_integers(self):
        assert multiply(6, 7) == 42

    def test_with_zero(self):
        assert multiply(99, 0) == 0

    def test_negatives(self):
        assert multiply(-3, -4) == 12

    def test_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)


class TestDivide:
    def test_exact(self):
        assert divide(20, 4) == 5

    def test_floats(self):
        assert divide(1, 4) == pytest.approx(0.25)

    def test_negative(self):
        assert divide(-9, 3) == -3

    def test_dividend_zero(self):
        assert divide(0, 5) == 0


# ---------- 除零错误 ----------

class TestDivisionByZero:
    def test_integer_zero_raises(self):
        with pytest.raises(DivisionByZeroError, match="除数不能为零"):
            divide(10, 0)

    def test_float_zero_raises(self):
        with pytest.raises(DivisionByZeroError):
            divide(1.5, 0.0)

    def test_zero_divided_by_zero_raises(self):
        with pytest.raises(DivisionByZeroError):
            divide(0, 0)

    def test_is_exception(self):
        # 自定义异常应可作为普通异常被捕获
        with pytest.raises(Exception):
            divide(1, 0)


# ---------- 输入校验 ----------

class TestInputValidation:
    @pytest.mark.parametrize("func", [add, subtract, multiply, divide])
    @pytest.mark.parametrize("bad_value", ["1", None, [1], {"a": 1}])
    def test_invalid_operand_type(self, func, bad_value):
        with pytest.raises(TypeError):
            func(bad_value, 1)
        with pytest.raises(TypeError):
            func(1, bad_value)

    def test_bool_rejected(self):
        # bool 虽是 int 的子类，但计算器应拒绝
        with pytest.raises(TypeError):
            add(True, 1)

    def test_divide_by_zero_before_type_issue(self):
        # 两个操作数合法时，除零抛专用异常而非 TypeError
        with pytest.raises(DivisionByZeroError):
            divide(1, 0)
