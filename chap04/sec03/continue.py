# continue 키워드

# 변수를 선언합니다.
numbers = [5, 15, 6, 20, 7, 25]

# 반복을 돌립니다.
for number in numbers:
  # number 가 10보다 작으면 다음 반복으로 넘어갑니다.
  if number < 10:
    continue
  # 출력합니다.
  print(number)


# if else 구문을 사용해도 되지만
# continue 키워드를 사용하면 이후 처리의 들여쓰기를 하나 줄일 수 있다.
'''
# 출력값
15
20
25
'''