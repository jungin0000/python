from Character import Hero, Monster
from Battle import Battle

def main():
    print("게임 시작")
    name = input("이름 입력 : ")
    role = input("직업 입력(전사/마법사/궁수) : ")
    hero = Hero(name, hp = 100, Attack = 20, Defense = 5, Role = Role)
    print(hero)

    monster = Monster(name = "고블린", hp = 50, Attack = 10, Defense = 2)
    print(monster)

    battle = Battle()
    battle.fight(hero, monster)

    print("\n전투 후 영웅 상태 : ")
    print(hero)

    if __name__ == '__main':
        main()