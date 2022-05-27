# 리스트 안에 for문 사용하기

# 리스트를 선언합니다.
array_1 = [i * i for i in range(0, 20, 2)]
# range(0, 20, 2)의 요소를 i라고 할 때
# i*i로 리스트를 재조합 해주세요 라는 코드이다.
# 이런 구문을 리스트 내포(list comprehensions)라고 부른다.

array_2 = [i for i in range(10)]
array_3 = [1 for i in range(10)]

# 출력합니다.
print(array_1)
print(array_2)
print(array_3)




'''
# 출력값
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
'''