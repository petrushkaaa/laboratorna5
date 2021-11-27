import pandas as pd
import collections
class Translator():
    def method(self, x:str ,y:float,c:float):
        self.x=x
        self.y=y
        self.c=c
        print(self.x, self.y, self.c)
    def method2(self, x:str ,y:float,c:float):
        self.x=x
        self.y=y
        self.c=c
        print(self.x, self.y)
t=Translator()
print("Декілька варіантів перекладу:")
t.method("Nonplussed", "огорошенный", "не удивленный")
print("Переклад слова")
t.method2("Left", "покидать","забывать")
