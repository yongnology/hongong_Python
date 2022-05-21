# 조건문 기본 사용

# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 양수 조건
if number > 0:
  print("양수입니다.")

if number < 0 :
  print("음수입니다.")

if number == 0:
  print("0 입니다.")

'''
# 출력값
정수 입력> 273
양수입니다.

# 출력값
정수 입력> 0
0 입니다.

# 출력값
정수 입력> -52
음수입니다.
'''