

from typing import Any


def foo() -> str:
    return 'foo'


def greet(name: str):
    return 'Hello {}'.format(name)


def add(a:int, b:int) -> int:
    return a + b


def power(base:int|float, exponent: int = 2):
    return base ** exponent

 
def summation(*args: Any):
    return sum(args)


def user_info(**kwargs):
    for k, v in kwargs.items():
        print('{}: {}'.format(k, v))


