# 끝자리로 짝수와 홀수 구분

# 입력을 받습니다.
number = input("정수 입력> ")

# 마지막 자리 숫자를 추출
last_charcter = number[-1]

# 숫자로 변환하기
last_number = int(last_charcter)

# 짝수 확인
if last_number == 0 \
  or last_number == 2\
  or last_number == 4\
  or last_number == 6\
  or last_number == 8:
  print("짝수입니다.")

# 홀수 확인하기
if last_number == 1 \
  or last_number == 3\
  or last_number == 5\
  or last_number == 7\
  or last_number == 9:
  print("홀수입니다.")

'''
# 출력값
정수 입력> 52
짝수입니다.

정수 입력> 273
홀수입니다.
'''