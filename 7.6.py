z=["ab","ba"]
m=z[::-1]
n=""
for i in m:
    for k in z:
        if (i==k):
            n="true"
        else:
            n="false"
print(n)                