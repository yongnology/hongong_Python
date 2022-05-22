# 확인문제 02
# 리스트를 조합해서 하나의 딕셔너리를 만들어보세요

key_list = ["name", "hp", "mp", "level"]
value_list = ["가사", 200, 30, 5]
character = {}

# 작성합니다.
for i in range(len(value_list)):
  character[key_list[i]] = value_list[i]

# 최종 출력
print(character)


# range를 사용하면 원할하다.
'''
# 출력값
{'name': '가사', 'hp': 200, 'mp': 30, 'level': 5}
'''