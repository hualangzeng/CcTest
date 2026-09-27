"""简易计算器：支持加减乘除，带输入校验和除零异常处理。"""


class CalculatorError(Exception):
    """计算器相关错误的基类。"""


class DivisionByZeroError(CalculatorError):
    """除数为零时抛出。"""


def _validate_number(value, name: str):
    """校验输入是否为数字（bool 不算合法数字）。"""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} 必须是数字，收到: {value!r} ({type(value).__name__})")


def add(a, b):
    """加法。"""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a, b):
    """减法。"""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a, b):
    """乘法。"""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a, b):
    """除法，除数为零时抛出 DivisionByZeroError。"""
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise DivisionByZeroError("除数不能为零")
    return a / b


def main():
    """简单的交互式命令行入口。"""
    operations = {
        "1": ("加法", add),
        "2": ("减法", subtract),
        "3": ("乘法", multiply),
        "4": ("除法", divide),
    }

    print("简易计算器")
    print("1. 加法  2. 减法  3. 乘法  4. 除法")
    choice = input("请选择运算 (1/2/3/4): ").strip()
    if choice not in operations:
        print(f"无效的运算选项: {choice}")
        return

    try:
        a = float(input("请输入第一个数: "))
        b = float(input("请输入第二个数: "))
    except ValueError:
        print("输入错误：请输入有效的数字")
        return

    name, func = operations[choice]
    try:
        result = func(a, b)
    except DivisionByZeroError as exc:
        print(f"运算失败：{exc}")
        return

    print(f"{name}结果: {result}")


if __name__ == "__main__":
    main()
