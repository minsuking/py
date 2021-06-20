import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.stdin=open(myPath+"/input.txt","rt")
'''
k번째 약수
n, k=map(int,input().split())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
    if count==k:
        print(i)
        break
else:
    print(-1)
'''
'''
K번째 수
T = int(input())
for t in range(T):
    n, s, e, k=map(int,input().split())
    a=list(map(int,input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1,a[k-1]))
'''
'''
k번째 큰수

n, m=map(int,input().split())
a=list(map(int,input().split()))
res=set()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            res.add(a[i]+a[j]+a[k])
res=list(res)
res.sort(reverse=True)
print(res[m-1])
'''
'''
최솟값 구하기

arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMin=float('inf')
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]
    
print(arrMin)
'''
'''
4.대표값

n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n + 0.5
ave = int(ave)
min=9999999
minIdx=-1
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        minIdx=idx
    elif tmp==min:
        if x>score:
            min=tmp
            score=x
            minIdx=idx

print(ave, minIdx+1)

a = 4.50000
print(round(a))
'''
'''
5. 정다면체

n, m=map(int,input().split())
max = 0
cnt=[0]*(n+m+3)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]=cnt[i+j]+1
for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]

for i in range(n+m+1):
    if max==cnt[i]:
        print(i, end=' ')
'''
'''
6. 자릿수의 합
'''
T = input()
a=list(map(int,input().split()))
maxNum = 0
max = 0

def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum 

for x in a:
    tot=digit_sum(x)
    if max<tot:
        max=tot
        maxNum=x
print(maxNum)