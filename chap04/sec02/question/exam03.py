# 확인문제 03

# 숫자는 무작위로 입력해도 상관없습니다.
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

# 가장 많이 나오는 코드이다.
for number in numbers:
  if number in counter:
    counter[number] += 1
  else:
    counter[number] = 1

# 최종 출력
print(counter)

'''
# 출력값
{1: 3, 2: 4, 6: 1, 8: 2, 4: 3, 3: 3, 9: 3, 5: 2, 7: 2}
'''