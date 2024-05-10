
num=3

fcount=1

for fa in range(1, num+1):
    if num%fa==0:
        fcount += 1
print("prime" if fcount==2 else "NotPrime"
