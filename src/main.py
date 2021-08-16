
from constants.constants import OPERATOR
from expressions.expressions import BinaryExp, NumericConstant


def step1():
    binary_expression = BinaryExp(NumericConstant(5), NumericConstant(10), OPERATOR.MUL)
    print(binary_expression.evaluate(None))

def step2():
    expression = BinaryExp(NumericConstant(5), BinaryExp(NumericConstant(30), NumericConstant(50), OPERATOR.PLUS), OPERATOR.PLUS)
    print(expression.evaluate(None))

if __name__ == "__main__":
    # step1()
    step2()
