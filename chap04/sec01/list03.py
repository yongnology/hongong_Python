# 리스트 연결 연산자와 요소 추가의 차이

list_a = [0, 1, 2, 3, 4, 5]
print("기존 list_a : ", list_a)
print()
print("# 리스트의 요소 하나 제거하기")

# 인덱스로 제거
# 제거 방법[1] - del 연산자
del list_a[1]
print("del list_a[1]: ", list_a)

# 제거 방법[2] - pop() 함수
# 아무값도 입력하지 않으면 -1이 되입되어 마지막이 삭제.
list_a.pop(2)
print("pop(2) : ", list_a)

'''
# 출력값
기존 list_a :  [0, 1, 2, 3, 4, 5]

# 리스트의 요소 하나 제거하기
del list_a[1]:  [0, 2, 3, 4, 5]
pop(2) :  [0, 2, 4, 5]
'''