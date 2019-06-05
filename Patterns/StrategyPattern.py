from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_business_logic(self):
        print("Working according to chosen %s's plan." % self._strategy)
        result = self._strategy.do_algorithm(['d', 'da', '3s', 'vm', 'a', 'da9'])
        print(''.join(str(i) for i in result))


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    class Meta:
        verbose_name = 'Strategy A'

    def do_algorithm(self, data: List):
        return sorted(data)

    def __str__(self):
        return self.Meta.verbose_name


class ConcreteStrategyB(Strategy):
    def __init__(self):
        self._name = 'Strategy B'

    def do_algorithm(self, data: List):
        return reversed(sorted(data))

    def __str__(self):
        return self._name


context = Context(ConcreteStrategyA())
context.do_business_logic()

context.strategy = ConcreteStrategyB()
context.do_business_logic()

