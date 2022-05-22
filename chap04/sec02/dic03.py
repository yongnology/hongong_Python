# 딕셔너리에 요소 제거하기

# 딕셔너리를 선어합니다.
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임"
}

# 요소 제거 전에 내용을 출력해 봅니다.
print("요소 제거 이전 : ", dictionary)

# 딕셔너리의 요소를 제거합니다.
del dictionary["name"]
del dictionary["type"]

# 요소 제거 후에 내용을 출력해 봅니다.
print("del diction")
print("요소 제거 이후 : ", dictionary)

'''
# 출력값
요소 제거 이전 :  {'name': '7D 건조 망고', 'type': '당절임'}
del diction
요소 제거 이후 :  {}
'''