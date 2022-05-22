# 리스트에 요소 추가하기

# 리스트를 선언합니다.
list_a = [1, 2, 3]
print("# 기본 list_a")
print(list_a)
print()

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)

'''
# 출력값
# 기본 list_a
[1, 2, 3]

# 리스트 뒤에 요소 추가하기
[1, 2, 3, 4, 5]

# 리스트 중간에 요소 추가하기
[10, 1, 2, 3, 4, 5]
'''