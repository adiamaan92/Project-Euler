
r=[]
f=[2,3,5,7,11,13,17,19]
temp = 1

for i in range(2,21,1):
    m=i
    #hile(m>1):
    for e in f:
        if m % e == 0:
            m=m/e
            r.append(e)
        

for e in r:
    temp = temp*e
    
r.sort()

print(r)
# t=0
# cnt=0
# # for e in r:
#     if e=t:
#         cnt=cnt+1
#     
print(temp)
    
        
        
