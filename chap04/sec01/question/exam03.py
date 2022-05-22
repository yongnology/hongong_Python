# 확인문제 03

numbers = [273, 105, 5, 32, 65, 9, 72, 800, 99]

# 짝수 홀수 구분
for number in numbers:
  if number % 2 == 0 :
    print("{}는 짝수입니다.".format(number))
  else:
    print("{}는 홀수입니다.".format(number))

print("-----------------")

# 다른방법
'''
for number in numbers:
  holzzak = ["짝수", "홀수"]
  print("{}는 {}입니다.".format(number, holzzak[number % 2]))
  # number % 2로 인해 짝수이면 0을 출력. 따라서 holzzak의 0번째 index 출력을 한다.
'''
print("-----------------")

# 자리수 출력
for number in numbers:
  print("{}는 {} 자리 수 입니다.".format(number, len(str(number))))

'''
# 출력값
273는 홀수입니다.
105는 홀수입니다.
5는 홀수입니다.
32는 짝수입니다.
65는 홀수입니다.
9는 홀수입니다.
72는 짝수입니다.
800는 짝수입니다.
99는 홀수입니다.
-----------------
273는 3 자리 수 입니다.
105는 3 자리 수 입니다.
5는 1 자리 수 입니다.
32는 2 자리 수 입니다.
65는 2 자리 수 입니다.
9는 1 자리 수 입니다.
72는 2 자리 수 입니다.
800는 3 자리 수 입니다.
99는 2 자리 수 입니다.
'''