# def end(state, cnt):
#     if state:
#         print(f'{cnt + 1}회 만에 성공')
#     else:
#         print('실패')
#     return cnt + 1

#
# personalNumber = list(range(1, 100))
# num_list = []
# for i in personalNumber:
#     print()
#     caseNumber = 100
#     print(i, '제공되는 숫자 ')
#     count = 0
#     comNumber = round(caseNumber / 2)
#     previousNumber = comNumber
#     upNumber = caseNumber
#     downNumber = 0
#     while True:
#         # print(upNumber, '^^^^^', downNumber)
#         # result = input(f'컴퓨터가 생각한 숫자 {comNumber} : \n 업 and  다운 and 정답=>')
#         if i == comNumber:
#             print('+++++++++++++++++++++++++++++++++++++맞췄습니다.++++++++++++++++++++++++++++++++++++++++++++')
#             num_list.append(end(True, count))
#             break
#
#         elif i > comNumber:
#             print(comNumber ,': 업')
#             downNumber = comNumber
#             comNumber = round(((upNumber - downNumber) / 2) + downNumber)
#
#             print('다음예상숫자 : ', comNumber, ' 이전 높은 숫자 : ', upNumber, ' 이전 낮은 숫자 : ', downNumber, )
#             count += 1
#
#         elif i < comNumber:
#             print(comNumber, ': 다운')
#             upNumber = comNumber
#             comNumber = round(((comNumber - downNumber) / 2) + downNumber)
#
#             print('다음예상숫자 : ', comNumber, ' 이전 높은 숫자 : ', upNumber, ' 이전 낮은 숫자 : ', downNumber, )
#             count += 1
#         else:
#             print('정확히 입력 하세요')
#
#     if count >= 15:
#         num_list.append(end(True, count))
#         break
#     elif count == 4:
#         print('마지막 기회 입니다.')
# print(sorted(num_list,reverse=True))

def end(state, cnt):
    if state:
        print(f'{cnt + 1}회 만에 성공')
    else:
        print('실패')
    return cnt + 1


personalNumber = int(input('업 & 다운 넘버 정하기: '))
num_list = []
i = personalNumber
print()
caseNumber = 100
print(i, '제공되는 숫자 ')
count = 0
comNumber = round(caseNumber / 2)

upNumber = caseNumber
downNumber = 0
while True:
    # print(upNumber, '^^^^^', downNumber)
    result = input(f'컴퓨터가 생각한 숫자 {comNumber} : \n 업 and  다운 and 정답=>')
    if i == comNumber and result == '정답':
        print('+++++++++++++++++++++++++++++++++++++맞췄습니다.++++++++++++++++++++++++++++++++++++++++++++')
        end(True, count)
        break

    elif i > comNumber and result == '업':

        downNumber = comNumber
        comNumber = round(((upNumber - downNumber) / 2) + downNumber)

        # print('다음예상숫자 : ', comNumber, ' 이전 높은 숫자 : ', upNumber, ' 이전 낮은 숫자 : ', downNumber, )
        count += 1

    elif i < comNumber and result == '다운':

        upNumber = comNumber
        comNumber = round(((comNumber - downNumber) / 2) + downNumber)

        # print('다음예상숫자 : ', comNumber, ' 이전 높은 숫자 : ', upNumber, ' 이전 낮은 숫자 : ', downNumber, )
        count += 1
    else:
        print('정확히 입력 하세요')

    if count >= 5:
        end(False, count)
        break
    elif count == 4:
        print('--마지막 기회 입니다.--')
