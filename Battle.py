class Battle:
    def fight(self, hero, monster):
        print(f"전투시작 {hero.name} vs {monster.name}")
        trun = 1

        while hero.is_alive() and monster.is_alive():
            print(f"==턴 {trun} ==")

            damage = monster.take_damage(hero.Attack)
            print(f"{hero.name}가 {monster.name}에게 {damage}의 데미지를 입힘")

            if not monster.is_alive():
                print(f"몬스터 죽음")
                print(f"{hero.name}가 경험치 10얻음")
                return

            damage = hero.take_damage(monster.Attack)
            print(f"{hero.name}가 {monster.name}에게 {damage}의 데미지를 입힘")
            if not hero.is_alive():
                print(f"히어로 죽음")
                return

            trun += 1