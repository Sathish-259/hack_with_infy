a=int(input())
l=list(map(int,input().split()))
s=0
d=[]
for i in range(a):
    for j in range(a-1):
        if l[j]>l[j+1]:
            d.append(l[j]-l[j+1])
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
print(max(d))
