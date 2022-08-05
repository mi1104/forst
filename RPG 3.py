import random

def creat_char(): #캐릭터 만드는 함수
    print("캐릭터를 생성합니다")
    print("당신의 직업을 선택해 주세요")
    job_list = ["전사", "마법사"]
    job = input("전사와 마법사 중 선택하실 수 있습니다 >> ")
    while True:
        if job in job_list:
            break
        # elif job == "마법사":
        #     break
        else:
            job = input("전사와 마법사 중 선택하실 수 있습니다 >> ")

    print(f"당신은 {job}직업을 선택했습니다.")
    answer = input("계속할까요? 예/아니오 ")
    return answer, job

class Rpg:
    def __init__(self, name, atk, max_hp, hp, level, xp):
        self.name = name
        self.atk = atk
        self.max_hp = max_hp
        self.hp = hp
        self.level = level
        self.xp = xp


######################################################

answer = "아니오"
print("RPG에 오신 것을 환영합니다")
print("제작: 성")
print("스토리: 성")

#캐릭터 생성

answer, job = creat_char() # ("예", "전사")

player = Rpg(job, 10, 100, 100, 1, 0)

slime = Rpg("슬라임", 3, 90, 90, 1, 5)

ghost = Rpg("처녀귀신", 10, 120, 120, 1, 10)

black_dragon = Rpg("흑룡", 150, 1000, 1000, 100, 1000)


xp_list = [i ** 3 for i in range(2, 100)]
# 모험
while True:
    random_int = random.random() * 100
    if random_int <= 50:
        monster = slime
    elif random_int > 50 and random_int < 90:
        monster = ghost
    else:
        monster = black_dragon


    print(f"{monster.name}을 만났습니다.")
    monster.hp = monster.max_hp
    
    player_sel = input("싸운다 / 집에간다")
    if player_sel == "싸운다":
        while True:     # 모험 - 전투 - "싸운다"
            print(f"{player.name}의 상태")
            print(f"Level : {player.level}")
            print(f"HP : {player.hp}/{player.max_hp}")
            print(f"XP : {player.xp}")
            print(f"공격력 : {player.atk}")
            print("------------------------")
            print(f"{monster.name}의 상태")
            print(f"Level : {monster.level}")
            print(f"HP : {monster.hp}/{monster.max_hp}")
            print(f"공격력 : {monster.atk}")
            print("------------------------")

            player_move = input("공격하려면 attack을 입력해주세요>> ")
            # 플레이어의 공격
            print(f"{monster.name}을 공격합니다")
            print(f"{monster.name}이 {player.atk}의 데미지를 입었습니다")
            monster.hp = monster.hp - player.atk
            if monster.hp <= 0:
                print(f"{monster.name}을 물리쳤습니다.")
                print(f"경험치를 {monster.xp} 얻었습니다.")
                player.xp = player.xp +monster.xp
                if player.xp > xp_list[player.level]:
                    print(f"{player.name}의 레벨이 올랐습니다.")
                    player.level += 1
                    print(f"{player.name}의 공격력이 올랐습니다.")
                    player.atk += 10
                    print(f"{player.name}의 hp가 올랐습니다.")
                    player.max_hp += 50
                break
            
            #몬스터의 공격
            print(f"{monster.name}이 공격합니다")
            print(f"{player.name}가 {monster.atk}의 데미지를 입었습니다.")
            player.hp = player.hp - monster.atk
            if player.hp <= 0:
                print(f"{monster.name}에게 졌습니다.")
                print(f"경험치를 {player.xp/3} 잃었습니다.")
                player.xp = player.xp - player.xp/3
                break
    elif player_sel == "집에간다":
        print(f"{player.name}는 집에 갑니다")
        print(f"{player.name}의 HP가 회복되었습니다")
        player.hp = player.max_hp
