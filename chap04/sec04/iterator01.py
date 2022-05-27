# reversed()함수와 이터레이터

# 변수를 선언합니다.
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

# reversed_numbers를 출력합니다.
print("reversed_numbers : ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

'''
# 출력값
reversed_numbers :  <list_reverseiterator object at 0x000001E73C2A7C40>
6
5
4
3
2
1
'''