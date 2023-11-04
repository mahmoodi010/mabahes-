def aq(z):
    if(z==0):
        print(z)
        return(1)
    else:
        print(z)
        return z*aq(z-1)
aq(3)