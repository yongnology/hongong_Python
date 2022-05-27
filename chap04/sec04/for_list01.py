# 반복문을 사용한 리스트 생성

# 변수를 선언합니다.
array = []

# 반복문을 적용합니다.
for i in range(0, 20, 2):
  array.append(i * i)

# 출력합니다.
print(array)


# range(0, 20, 2)로 0부터 20사이의 짜수를 구한 뒤,
# 제곱해서 새로운 리스트를 만드는 것이다.

'''
# 출력값
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
'''