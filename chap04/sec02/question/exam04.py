# 확인문제 04

# 딕셔너리를 선언합니다.
charcter = {
  "name" : "기사",
  "level" : 12,
  "item" : {  # 딕셔너리
    "sword" : "불꽃의 검",
    "armor" : "풀플레이트"
    },
  "skill" : ["배기", "세게 배기", "아주 세게 베기"] # 리스트
}

# for 반복문을 사용합니다.
for key in charcter:
  if type(charcter[key]) is dict: # 딕셔너리 타입인 경우
    for k in charcter[key]:
      print("{} : {}".format(k, charcter[key][k]))

  elif type(charcter[key]) is list: # 리스트 타입인 경우
    for item in charcter[key]:
      print("{} : {}".format(key, item))

  else:
    print("{} : {}".format(key, charcter[key]))

'''
# 출력값
name : 기사
level : 12
sword 불꽃의 검
armor 풀플레이트
skill : 배기
skill : 세게 배기
skill : 아주 세게 베기
'''
