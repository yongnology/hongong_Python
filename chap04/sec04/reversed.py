# reversed() 함수

# 리스트를 선언하고 뒤집습니다.
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

# 출력합니다.
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5]):", list(list_reversed))
print()

# 반복문을 적용해 봅니다.
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
  print("-", i)

'''
# 출력값
 reversed() 함수
reversed([1, 2, 3, 4, 5]): <list_reverseiterator object at 0x0000018323327C40>
list(reversed([1, 2, 3, 4, 5]): [5, 4, 3, 2, 1]

# reversed() 함수와 반복문
for i in reversed([1, 2, 3, 4, 5]):
- 5
- 4
- 3
- 2
- 1
'''