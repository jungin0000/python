from abc import ABC, abstractmethod
import random


class Monster(ABC):
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    @abstractmethod
    def special_attack(self):
        pass

    @abstractmethod
    def description(self):
        pass


class Goblin(Monster):
    def special_attack(self):
        return f"{self.name}의 독 공격! 공격력이 {self.attack_power * 1.5}로 증가!"

    def description(self):
        return f"{self.name}: 작고 교활한 몬스터. 빠른 움직임이 특징."


class Orc(Monster):
    def special_attack(self):
        return f"{self.name}의 망치 강타! 공격력이 {self.attack_power * 2}로 증가!"

    def description(self):
        return f"{self.name}: 강인하고 거친 몬스터. 강력한 힘이 특징."


class Dragon(Monster):
    def special_attack(self):
        return f"{self.name}의 화염 숨결! 공격력이 {self.attack_power * 3}로 증가!"

    def description(self):
        return f"{self.name}: 거대하고 위엄 있는 몬스터. 불을 내뿜는 능력이 특징."


def battle(monster):
    print(monster.description())
    print(monster.special_attack())


monsters = [
    Goblin("고블린", 10),
    Orc("오크", 20),
    Dragon("드래곤", 50),
]


for _ in range(5):  
    monster = random.choice(monsters)
    print("\n새로운 전투 시작!")
    battle(monster)
