# in 문자열 연산자를 활용해서 짝수와 홀수 구분

# 입력을 받습니다.
number = input("정수 입력>")
last_character = number[-1]

# 짝수 조건
if last_character in "02468" :
  print("짝수입니다.")
  
# 홀수 조건
if last_character in "13579" :
  print("홀수입니다.")

'''
# 출력값
정수 입력>52
짝수입니다.
'''