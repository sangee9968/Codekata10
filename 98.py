n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if l[i]>l[i+1]:
        break
#print result        
print(i)    
    
