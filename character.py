class Character:
    def __init__(self, name, hp, Attack, Defense):
        self.name = name
        self.hp = hp
        self.Attack = Attack
        self.Defense = Defense

    def take_damage(self, damage):
        self.hp = (self.Defense + self.hp) - damage

    def is_alive(self):
        if self.hp <= 0:
            print("캐릭터가 죽음")
        else:
            print("아직 살아있음")

    def __str__(self):
        return (f"{self.name}, HP : {self.hp}, 공격력 : {self.Attack}, 방어력 : {self.Defense}")


class Hero(Character):
    def __init__(self, Role, exp, name, hp, Attack, Defense):
        super().__init__(name, hp, Attack, Defense)
        self.Role = Role
        self.exp = 0

    def gain_exp(self, amount):
        self.exp += amount

    def special_attack(self):

        if self.Role == "전사":
            return self.Attack + 4
        elif self.Role == "마법사":
            return self.Attack + 3
        elif self.Role == "궁수":
            return self.Attack + 2
        else:
            return self.Attack


class Monster(Character):
    def __init__(self, name, hp, Attack, Defense):
        super().__init__(name, hp, Attack, Defense)