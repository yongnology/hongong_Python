# 5초 동안 반복하기

# 시간과 관련된 기능을 가져옵니다.
import time

# 변수를 선언합니다.
number = 0

# 5초 동안 반복합니다.
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

# 출력합니다.
print("5초동안 {}번 반복했습니다.".format(number))


# 통신할 때 자주 사용되는 코드이다.
# 시간을 기반으로 조건을 걸 때 while 반복문을 활용한다는 것 기억하기.

'''
# 출력값
5초동안 83379150번 반복했습니다.
'''