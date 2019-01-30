n=int(input())
p=1
while n>0:
    r=n%10
    p=p*r
    n=n//10
#print result    
print(p)
