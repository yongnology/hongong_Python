# 날짜/시간 출력하기

# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

'''
# 출력값
2022 년
5 월
20 일
18 시
44 분
57 초
'''