'''
리스트와 내장함수(1)
'''
import random as r
a=[]
#print(a)
b = list()
#print(a,b)


a=[1,2,3,4,5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c = a+b
#print(c)


print(a)
a.append(6)
print(a)

a.insert(3, 7)
print(a)

t = a.pop()
print(b)

t = a.pop(3)
print(t)

print(a)

a.remove(4)
print(a)

print(a.index(5))

a=list(range(1,11))
sum = sum(a)
maxNum = max(a)
minNum = min(a)
print(maxNum)
print(minNum)
r.shuffle(a)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.clear()
print(a)
