'''
리스트와 내장함수(2)
'''

a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
print()


for x in enumerate(a): 
    print(x)

#자리에 어떤값이 있는지 알려주는것
#(0,23) (1,12) ...(4,19)
#enumerate는 튜플로 만들어줌

b = (1,2,3,4,5)
print(b[0])

#list와 다른점은 예를들어 b[0]=7을 하면 에러가남. 
#튜플값은 변경이 절대 안됨

#b[0]=7
print(b[0])

for x in enumerate(a):
    print(x[0],x[1])
print()

for index, value in enumerate(a):
    print(index,value)
print()

if all(60>x for x in a):
    print("YES")
else:
    print("NO")

if any(50>x for x in a):
    print("YES")
else:
    print("NO")

#공부를 이만큼이나 했는데 안된다고? github test
    


