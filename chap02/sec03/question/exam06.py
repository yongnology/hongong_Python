# 확인문제 6

a = input("문자열 입력> ")
b = input("문자열 입력> ")

print(a, b)

c = b
b = a
a = c

print(a, b)

'''
# 출력값
문자열 입력> 5
문자열 입력> 3
5 3
3 5
'''