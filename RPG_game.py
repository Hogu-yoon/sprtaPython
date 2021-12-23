# name = 'minigoblin'
# hp = 10
# att = 10
#
# name = 'goblin'
# hp = 30
# att = 30
#
# name = 'supergoblin'
# hp = 50
# att = 50
#
# name = 'warrior'
# hp = 100
# att = 10


class Object:
    def __init__(self, name, hp, att):
        self.name = name
        self.hp = hp
        self.att = att
        self.max_hp = hp

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.att
        if enemy.hp <= 0:
            enemy.hp = 0
        name = self.name
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f'{name}이(가) {enemy.name}을(를) 공격!')
        print(f'{enemy.name}에게 {self.att}만큼의 데미지!!!')
        print(f'{enemy.name}의 HP가 {enemy.hp} 이 되었습니다.')
        return enemy.hp

    def info(self):
        return f'{self.name}의 체력{self.hp}'


class Monster(Object):
    def wait(self):
        name = self.name
        print(f'{name}이 대기합니다.')
        return

    def healing(self):
        name = self.name
        self.hp += 10
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        print(f'{name}이 치료합니다.')
        return


class Player(Object):
    def magic(self, enemy):
        enemy.hp = enemy.hp // 2
        if enemy.hp <= 0:
            enemy.hp = 0
        name = self.name
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print(f'{name}이(가) {enemy.name}을(를) 마법공격!')
        print(f'{enemy.name}의  체력 절반 만큼을 감소 시킵니다~')
        print(f'{enemy.name}의 HP가 {enemy.hp} 이 되었습니다.')
        return enemy.hp


import random
import time

# 플레이어 생성 이름 체력 공격력
player = Player('전사', 100, 30)
# 몬스터 생성 이름 체력 공격력
mini_goblin = Monster('작은고블린', 10, 10)
# 몬스터 생성 이름 체력 공격력
goblin = Monster('고블린', 30, 30)
# 몬스터 생성 이름 체력 공격력
super_goblin = Monster('고블린족장', 50, 50)

# 몬스터 리스트 생성 추후 상태에 따라 제거해나가면 승리
monster_list = [mini_goblin, goblin, super_goblin]


# if문만으로 불편해서 케이스문을 구현했으나 죽은 몬스터도 공격가능한 문제로 삭제예정
def switch(x):
    result = {mini_goblin.name: mini_goblin, goblin.name: goblin, super_goblin.name: super_goblin}
    if x in result:
        result = result.get(x)
        return result
    else:
        print('공격대상이 없습니다.')
        return


def player_turn(m_list):
    print("------------------플레이어 턴--------------------")
    print(player.info())
    time.sleep(1)
    att = input('공격 || 마법공격 ===>')
    while True:
        for monster in m_list:
            print(monster.name)
        who = input('공격대상의 이름은 ? ===>')
        att_target = switch(who)
        # 공격할 대상이 있다면 빠져나와서 공격
        if att_target is not None:
            break
    if att == '공격':
        player.attack(att_target)
    elif att == '마법공격':
        player.magic(att_target)
    else:
        print('공격 실패 턴을 넘 깁니다.')



def monster_turn(mob_list):
    print("------------------몬스터 턴---------------------")
    for monster in mob_list:
        rand_mob_num = random.randrange(0, 3)
        time.sleep(1)
        if rand_mob_num == 0:
            monster.healing()

        elif rand_mob_num == 1:
            monster.wait()

        elif rand_mob_num == 2:
            monster.attack(player)



def monster_check():
    monsters = []
    for monster in monster_list:
        if monster.hp == 0:
            print(f'{monster.name}이 죽었습니다.')
            monsters.append(monster)
    mon_list = [x for x in monster_list if x not in monsters]
    return mon_list


def player_check():
    if player.hp <= 0:
        print('플레이어가 사망하였습니다 \n-----YOU DIED----- \n-------패배--------')
        return False
    return True


# 실행 부
print("-----------------------------------------------")
print(player.info())
print(mini_goblin.info())
print(goblin.info())
print(super_goblin.info())

while True:
    player_turn(monster_list)
    monster_list = monster_check()
    monster_turn(monster_list)
    player_state = player_check()
    if not monster_list:
        print('모든 몬스터가 죽었습니다. \n전투에서 승리하였습니다.')
        break
    elif not player_state:
        break
