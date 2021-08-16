from abc import abstractmethod
from constants.constants import OPERATOR

from runtime.runtimecontext import RUNTIME_CONTEXT


class Exp():

    @abstractmethod
    def evaluate(self, context: RUNTIME_CONTEXT):
        pass

class NumericConstant(Exp):

    def __init__(self, value: float) -> None:
        self.__value = value

    def evaluate(self, context: RUNTIME_CONTEXT):
        return self.__value


class UnaryExp(Exp):

    def __init__(self, a: Exp, op: OPERATOR) -> None:
        self.__ex1 = a
        self.__op = op

    def evaluate(self, context: RUNTIME_CONTEXT):
        if self.__op == OPERATOR.PLUS:
            return self.__ex1.evaluate(context)
        elif self.__op == OPERATOR.MINUS:
            return -self.__ex1.evaluate(context)
        return float('NaN')

class BinaryExp(Exp):

    def __init__(self, a: Exp, b: Exp, op: OPERATOR) -> None:
        self.__ex1 = a
        self.__ex2 = b
        self.__op = op
        

    def evaluate(self, context: RUNTIME_CONTEXT):
        if self.__op == OPERATOR.PLUS:
            return self.__ex1.evaluate(context) + self.__ex2.evaluate(context)
        elif self.__op == OPERATOR.MINUS:
            return self.__ex1.evaluate(context) - self.__ex2.evaluate(context)
        elif self.__op == OPERATOR.MUL:
            return self.__ex1.evaluate(context) * self.__ex2.evaluate(context)
        elif self.__op == OPERATOR.DIV:
            return self.__ex1.evaluate(context) / self.__ex2.evaluate(context)
        
        return float('NaN')