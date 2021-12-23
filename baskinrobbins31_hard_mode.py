import random
import time
import threading


class GameSeq2:
    def __init__(self, game_number):
        # 모드처리 생성자
        mode = input("베스킨라빈스31 게임 모드 선택 easy or hard ===>")
        if mode.lower() == 'easy':
            mode = True
        elif mode.lower() == 'hard':
            mode = False
        else:
            print('정확하게 입력하세요 (easy로 실행)')
            mode = True
        # 게임 넘버
        self.game_number = game_number
        # 게임 시작 상태
        self.game_start = True
        # 게임 순서
        self.game_seq = True
        # 게임 승리 넘버
        self.victory_nums = [2, 6, 10, 14, 18, 22, 26, 30]
        # 현재 게임 승리넘버
        self.victory_num = 0
        # 모드 상태
        self.easy_mode = mode

    # 승리 넘버 생성 함수
    def victory_number(self, game_num):
        vic_nums = self.victory_nums
        vic_nums.append(game_num)
        vic_nums.sort()
        vic_num = vic_nums.index(game_num)
        vic_num = vic_nums[vic_num + 1]
        vic_num = vic_num - game_num
        self.victory_num = vic_num
        if vic_num == 0:
            vic_num = random.randrange(1, 4)
        print(vic_num)
        return vic_num

    # 랜덤으로 수를 생성해주는 함수
    def random_number(self, game_num):
        easy_mode = self.easy_mode
        if easy_mode:
            ran_number = random.randrange(1, 4)
        else:
            ran_number = self.victory_number(game_num)
        print("--컴퓨터 최적의 수 계산중--")
        lock = threading.Lock()
        try:
            # 쓰레드 동기화 : 비동기시 input 적용하면 except 발생
            lock.acquire()
            # 뭔가 하는 거 처럼 보이는 방법
            time.sleep(ran_number)
            # time.sleep(1)
        except ValueError:
            print('장난 치지 마세요')
        finally:
            # 동기화 작업 끝내기
            lock.release()
            for i in range(ran_number):
                game_num += 1
                print(f'컴퓨터 숫자 {game_num}')
                if game_num >= 31:
                    print('컴퓨터 의 패배 임니다.')
                    self.game_number = game_num
                    break
                self.game_number = game_num

    # 나의 숫자 처리 함수
    def user_number(self, user_num, game_num):
        if user_num > 3:
            user_num = 3

        for i in range(user_num):
            game_num += 1
            print(f'당신의 숫자 {game_num}')
            if game_num >= 31:
                print('당신의 패배 입니다.')
                self.game_number = game_num
                break
        self.game_number = game_num


# 컴퓨터와 나의 순번 정리해주는 함수
def game_sequence(state, game_num):
    if random.randrange(2) and state == True:
        return game_num
    else:
        try:
            game_num = int(input("참여하실 숫자(1,2,3)를 선택 하세요 ==>> "))
        except ValueError:
            print('숫자만 입력하세요')
            game_sequence(state, game_num)
        return game_num


# 시작 숫자 , easy_mode 선택

game = GameSeq2(0)

while True:
    # 순서 판별
    if game.game_seq:
        # 사용자 숫자 입력 및 순서 판별
        input_number = game_sequence(game.game_start, game.game_number)
        # 시작 값 저장
        game.game_start = False
        # 사용자 숫자 처리기
        game.user_number(input_number, game.game_number)
        # 사용자 턴 종료
        game.game_seq = False
    else:
        # 컴퓨터 숫자 처리기
        game.random_number(game.game_number)
        # 컴퓨터 턴 종료
        game.game_seq = True

    if game.game_number >= 31:
        break
