a=int(input())
b=a
ans=0
while a>0:
	ans=ans*10+a%10
	a=a//10
	#print(a,ans)
print(f'{b}+{ans}={b+ans}')