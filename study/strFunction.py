'''
문자열과 내장함수

'''

msg="It is Time"

print(msg.upper())
print(msg.lower())
print(msg)


tmp = msg.upper()
print(tmp.find('T')) #처음에 발견된 문자의 자릿수
print(tmp.count('T')) # 해당 문자가 포함된 숫자
print(msg[:2])
print(msg[3:5]) #[시작:끝] substring
print(len(msg)) #길이


for i in range(len(msg)):
    print(msg[i], end='')
print()

for x in msg:
    print(x,end= ' ')
print()


for x in msg:
    if x.isupper():     #대문자만 출력
        print(x, end=' ')
print()


for x in msg:
    if x.islower():     #소문자만 출력
        print(x, end=' ')
print()


tmp = 'AZ'
for x in tmp:
    print(ord(x)) #아스키 넘버

tmp = 65
print(chr(tmp)) #숫자에 관한 문자
