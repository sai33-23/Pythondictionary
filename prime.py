i=1
while i<=100:
    j=1
    factor=0
    while j<=i:
        if i%j==0:
            factor=factor+1
        j=j+1
    if factor==2:
        print(i,"is a prime number")
    else:
        print(i,"is not a prime number")
    i+=1
