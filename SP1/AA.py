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
