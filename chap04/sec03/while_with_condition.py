# 변수를 선언합니다.
list_test = [1, 2, 1, 2]
value = 2

# list_test 내부에 value가 있다면 반복
while value in list_test:
  list_test.remove(value)

# 출력합니다.
print(list_test)

# 리스트 내부에 있는 모든 2가 제거될 떄까지 반복하기 때문에
# 2가 모두 제거된 결과가 출력된다.

'''
# 출력값
[1, 1]
'''