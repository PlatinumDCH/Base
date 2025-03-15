from dataclasses import dataclass, field


@dataclass
class Dog:
    atribute_calass:str = field(default='testing', init=False) 
    name: str
    age: int

    def desciption(self) -> str:
        return f'{self.name} & {self.age}'
    
    def speak(self, sound: str) -> str:
        return f'{self.name} say {sound}'

"""
class Dog:
    atribute_class = testing

    def __init__(self, name, age):
        self.name = name
        self.age = age
"""
