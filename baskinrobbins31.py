# import random
# import time
# import threading
#
#
# class GameSeq:
#     def __init__(self, game_number, game_start, game_seq):
#         # 게임처리 클래스
#         # 게임 넘버
#         self.game_number = game_number
#         # 게임 시작 상태
#         self.game_start = game_start
#         # 게임 순서
#         self.game_seq = game_seq
#
#     # 랜덤으로 수를 생성해주는 함수
#     def random_number(self, beskin_number):
#         ran_number = random.randrange(1, 4)
#         print("--컴퓨터 최적의 수 계산중--")
#         lock = threading.Lock()
#         try:
#             # 쓰레드 동기화 : 비동기시 input 적용하면 except 발생
#             lock.acquire()
#             # 뭔가 하는 거 처럼 보이는 방법
#             # time.sleep(ran_number)
#             time.sleep(1)
#         except:
#             print('장난 치지 마세요')
#         finally:
#             #동기화 작업 끝내기
#             lock.release()
#             for i in range(ran_number):
#                 beskin_number += 1
#                 print(f'컴퓨터 숫자 {beskin_number}')
#                 if beskin_number >= 31:
#                     print('컴퓨터 의 패배 임니다.')
#                     self.game_number = beskin_number
#                     break
#                 self.game_number = beskin_number
#
#     def user_number(self, user_num, game_num):
#         if user_num > 3:
#             user_num = 3
#
#         for i in range(user_num):
#             game_num += 1
#             print(f'당신의 숫자 {game_num}')
#             if game_num >= 31:
#                 print('당신의 패배 입니다.')
#                 self.game_number = game_num
#                 break
#         self.game_number = game_num
#
#
# def game_sequence(state, game_num):
#     if random.randrange(2) and state == True:
#         return game_num
#     else:
#         try:
#             game_num = int(input("참여하실 숫자(1,2,3)를 선택 하세요 ==>> "))
#         except:
#             print('숫자만 입력하세요')
#             game_sequence(state, game_num)
#         finally:
#             return game_num
#     return game_num
#
#
# game = GameSeq(0, True, True)
#
# while True:
#     if game.game_seq:
#         input_number = game_sequence(game.game_start, game.game_number)
#         game.game_start = False
#         game.user_number(input_number, game.game_number)
#         game.game_seq = False
#     else:
#         game.random_number(game.game_number)
#         game.game_seq = True
#     if game.game_number >= 31:
#         break
