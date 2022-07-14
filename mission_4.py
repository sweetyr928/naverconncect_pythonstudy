# inp = input('Europe floor?')
# usf = int(inp) + 1
# print('US floor', usf)


k_age = int(input('한국 나이를 입력해주세요 : '))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))

if birth==0:
    a_age = int(k_age) - 1
else:
    a_age = int(k_age) - 2
print('미국나이 : ', a_age)
