
from constants.constants import OPERATOR
from expressions.expressions import BinaryExp, NumericConstant


binary_expression = BinaryExp(NumericConstant(5), NumericConstant(10), OPERATOR.MUL)
print(binary_expression.evaluate(None))