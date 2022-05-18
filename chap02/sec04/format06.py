# 소수점 아래 자리수 지정하기

output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)

'''
# 출력값
         52.273
          52.27
           52.3
'''