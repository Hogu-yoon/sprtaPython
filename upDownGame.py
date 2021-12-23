import random as rd

def end(state, cnt):
    if state:
        print(f'{cnt + 1}회 만에 성공')
    else:
        print('실패')

com = rd.randrange(1, 101)
print(com)
count = 0
while True:
    my_num = int(input())

    if com == my_num:
        print('맞췄습니다.')
        end(True, count)
        break

    elif com > my_num:
        print('업')
        count += 1

    elif com < my_num:
        print('다운')
        count += 1

    if count >= 5:
        end(False, count)
        break
    elif count >= 4:
        print('마지막 기회입니다.')