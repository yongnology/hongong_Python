# 조건을 활용한 내포

# 리스트를 선언합니다.
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

# 출력합니다.
print(output)


# array의 요소를 fruit이라고 할 때,
# 초콜릿이 아닌 fruit으로 리스트를 재조합 해주세요. 라는 코드이다.
# 따라서 실행하면 초콜릿을 제외한 요소만 모인 리스트를 만들어 준다.

'''
# 출력값
['사과', '자두', '바나나', '체리']
'''