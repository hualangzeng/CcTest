# CcTest

简易计算器 Python 小项目，支持加减乘除，包含输入校验、除零异常处理及 pytest 单元测试。

## 功能

- `add` / `subtract` / `multiply` / `divide` 四则运算
- 操作数类型校验（非数字抛出 `TypeError`）
- 除数为零时抛出自定义异常 `DivisionByZeroError`
- 提供交互式命令行入口

## 使用

```bash
python calculator.py
```

## 运行测试

```bash
pip install pytest
python -m pytest test_calculator.py -v
```
