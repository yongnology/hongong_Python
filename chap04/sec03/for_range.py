# for 반복문과 범위

# for 반복문과 범위를 함께 조합해서 사용합니다.
for i in range(5):
  print(str(i) + " = 반복 변수") 
print()

for i in range(5, 10):
  print(str(i) + " = 반복 변수")
print()

for i in range(0, 10, 3):
  print(str(i) + " = 반복 변수")
print()

'''
# 출력값
0 = 반복 변수
1 = 반복 변수
2 = 반복 변수
3 = 반복 변수
4 = 반복 변수

5 = 반복 변수
6 = 반복 변수
7 = 반복 변수
8 = 반복 변수
9 = 반복 변수

0 = 반복 변수
3 = 반복 변수
6 = 반복 변수
9 = 반복 변수
'''