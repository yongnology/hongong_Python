# 확인문제 05

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers :
  output[(number -1) % 3].append(number)

print(output)

'''
# 출력값
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''