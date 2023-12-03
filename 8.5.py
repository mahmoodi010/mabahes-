qw=["m","t","22","qq","@","&"]
print(qw)
for i in qw[:]:
    qw.pop(0)
print(qw)    
######################
qw=["m","t","22","qq","@","&"]
print(qw)
for i in qw[:]:
    del qw[:]
print(qw)
########################
qw=["m","t","22","qq","@","&"]
print(qw)
for i in qw[:]:
    qw.remove(i)
print(qw)              