# if 조건문과 긴 문자열

# 변수를 선언합니다.
number = int(input("정수 입력> "))

# if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수 입니다.".format(number, number))

'''
# 출력값
정수 입력> 10
입력한 문자열은 10입니다.
10는(은) 짝수입니다.
'''

# 들여쓰기 문제를 해결하기 위해 코드를 한줄로 적고 \n을 통해 줄바꿈을 구현한다.