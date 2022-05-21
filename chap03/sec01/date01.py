# 날짜/시간을 한 줄로 출력하기

# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
  now.year,
  now.month,
  now.day,
  now.hour,
  now.minute,
  now.second
))

'''
# 출력값
2022년 5월 20일 18시 48분 48초
'''