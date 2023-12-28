def sum(x,y):
    return x+y
def subtract(x,y):
    return x-y
def zarb(x,y):
    return x*y
def divide(x,y):
    return x/y
print("mashin hesab ")
adad1=float(input("adad 1 "))
adad2=float(input("adad 2:  "))
print("1.sum")
print("2.subtract")
print("1.zarb")
print("1.divide")
qwe=input("(1/2/3/4 )")
if qwe =="1":
    resalt = sum(adad1,adad2)
    op="+"
elif qwe =="2":
    resalt = subtract(adad1,adad2)
    op="-"    
elif qwe =="3":
    resalt = zarb(adad1,adad2)
    op="*"    
elif qwe =="4":
    resalt = divide(adad1,adad2)
    op="/"            
else:
    print("error")
    
print("resalt : {} {} {} ={}".format(adad1,op,adad2,resalt))        