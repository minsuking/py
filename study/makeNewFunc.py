'''
함수 만들기


함수는 항상 메인 스크립트보다 위에 작성을 해야한다.


def add(a, b):
    c = a+ b
    print(c)

add(3, 2)
add(5, 7)



def add(a, b):
    c = a + b
    return c

x = add(3, 2)
print(x)


def add(a, b):
    c=a+b
    d=a-b
    return c, d

print(add(3, 5))

'''
a=[12, 13, 7, 9, 19]

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

for v in a:
    if isPrime(v):
        print(v)
