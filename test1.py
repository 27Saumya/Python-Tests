from random import Random
from typing import Optional

class RandomClass(Random):
    def __init__(self, list: Optional[list]=None, num1: Optional[int]=7, num2: Optional[int]=77):
        super().__init__()
        self.list = list
        self.num1 = num1
        self.num2 = num2

    def randomChoose(self):
        return self.choice(self.list)

    def randomNum(self):
        return self.randint(self.num1, self.num2)

x = ["oof", "ye", "no", "fun", "enjoy", ":p"]

print(f"{RandomClass(list=x).randomChoose()}")
print(RandomClass().randomNum())