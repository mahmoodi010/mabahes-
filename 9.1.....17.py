a={"Ali":22,"Amin":31}
b=""
"Ali" in b
######################
a={"Ali":22,"Amin":31}
b=""
"31" in b
######################
a={"Ali":22,"Amin":31}
b=sorted(a)
print(a)
#####################
a={"Ali":22,"Amin":31}
b=sum(a)
#####################
a={5:21,11:28}
b=sum(a)
print(b)
#####################
a={"Ali":22,"Amin":31}
a.find("Amin")
#####################
a={"Ali":22,"Amin":31}
a.oppend(2)
#####################
a={"Ali":22,"Amin":31}
a.pop("Amin")
print(a)
#####################
a={"Ali":22,"Amin":31}
a.remove("Ali")
print(a)
#####################
def qw(a):
    b={"mohsen":21,"hossein":11,"reza":34}
    if a in b.values():
        print("ok")
    else:
        print("ok nis")
qw(85)
######################
def qw(a):
    b={"mohsen":21,"hossein":11,"reza":34}
    if a in b.values():
        print("ok")
    else:
        print("ok nis")
qw("reza")
#######################
a=["2","3","4"]
b=["5","6","7"]
c=[]
for i in zip(a,b):
    print(i)
    for h in i:
        print(h)
        c.append(h)
######################
a=["2","3","4"]
b=["5","6","7"]
c=[]
for i in zip(a,b):
    for h in i:
        c.append(h)
print(c)
################324###1#
def qw(a):
    if (a%2==0):
        print("2")
    else:
        print("1")
qw(85)
########################                    
name ="mahmoodi"
length=len(name)
print(length)
########################
import math as qw
def ddd(a,b,c):
    qwe=qw.sqrt((a-b)/c)
    return qwe
print(ddd(8,4,15))
#####################3
def aa(m,z):
    import math as s
    w=s.sin(m)+m.cos(z)
    print(w)
aa(4,12)    
#######################
aw="jbgdueghru"
a=""
b=""
for s in aw:
    if (s.islower()):
        a=a+s
    else:
        b=b+s
print(a)
print(b)        
####################
aa="mohsen"
qw=""
for d in aa:
    qw=d+qw
print(qw)    
##################
m=["mohsen","mahmoosi","21"]
z=m[::-1]
for n in z:
    print(n)
##################33
def qw(a):
    b=[]
    c=a[::-1]
    for i in c:
        b.append(i)
    print(b)
qw("hjfehj")
######################        
a="mahmoodii"
def qww(b):
    for i in range(len(a)):
        if a[i]==b:
            print(i)
            print("ok")
qww("a")     
#####################
def qw(value):
    return str(value)[::-1]
value1=input("adad1")
value2=input("adad2")
aqw=qw(value1)
if str(value2) in aqw:
    print("true")
else:
    print("false")    
#####################
                             


