s = 955
m=s
rev = 0
while(m>0):
    digit = m%10
    rev = rev*10+digit
    m = int(m/10)

print(rev)
if(rev == s):
    print('Palindrome !!!')
    
h=str(s)

a=''.join(reversed(h))
print(a)
if(a==h):
    print('Pal')
z='' 
for i in range(len(h)-1,-1,-1):
    z+=h[i]
    
print(z)