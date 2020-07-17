def diagonal(l,i,j,a,b):
    s=0
    i1=i-1
    j1=j+1
    for k in range(j+1,b):
        if i1<0 or j1==b:
            break
        if l[i1][j1]=='.':
            s+=1
        i1-=1
        j1+=1
    i1=i-1
    j1=j-1
    for k in range(j-1,-1,-1):
        if i1<0 or j1<0:
            break
        if l[i1][j1]=='.':
            s+=1
        i1-=1
        j1-=1
    i1=i+1
    j1=j+1
    for k in range(j+1,b):
        if i1==a or j1==b:
            break
        if l[i1][j1]=='.':
            s+=1
        i1+=1
        j1+=1
    i1=i+1
    j1=j-1
    for k in range(j-1,-1,-1):
        if i1==a or j1<0:
            break
        if l[i1][j1]=='.':
            s+=1
        i1+=1
        j1-=1
    return s
def row(l,i,j,a,b):
    s=0
    for k in range(b):
        if l[i][k]=='.':
            s+=1
    for k in range(a):
        if l[k][j]=='.':
            s+=1
    return s
a=int(input())
b=int(input())
l=[]
for i in range(a):
    l.append(list(map(str,input().split())))
s=0
for i in range(a):
    for j in range(b):
        if(l[i][j]=='.'):
            continue
        elif l[i][j]=='R':
            s+=row(l,i,j,a,b)
        elif l[i][j]=='B':
            s+=diagonal(l,i,j,a,b)
        elif l[i][j]=='Q':
            s+=row(l,i,j,a,b)
            s+=diagonal(l,i,j,a,b)
print(s)
            
