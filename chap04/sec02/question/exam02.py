# 확인문제 02

# 딕셔너리의 리스트를 선언합니다.
pets = [
{"name" : "구름", "age" : 5},
{"name" : "초코", "age" : 3},
{"name" : "아지", "age" : 1},
{"name" : "호랑이", "age" : 1}
]

print("# 우리 동네 애완 동물들")
for pet in pets:
  print("{} {} 살".format(pet["name"], pet["age"]))

'''
# 출력값
# 우리 동네 애완 동물들
구름 5 살
초코 3 살
아지 1 살
호랑이 1 살
'''