a=[]
b=[]
c=[]
v=["S","z","M","@","&","/","X","w","y"]
for i in v:
    if i.isupper():
        a.append(i)
    elif i.islower():
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)                