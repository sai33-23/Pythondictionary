from typing import Counter


a="mississippi"
b={}
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[i]:
            c=c+1
        j=j+1
    if a[i] not in b:
        b[a[i]]=c
    i=i+1
print(b)