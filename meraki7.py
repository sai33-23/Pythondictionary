d=[{"first":"1"},{"second":"2"},{"third":"1"},{"four":"5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
i=0
while i<len(d):
    k=d[i]
    for x in k:
        if x=="first":
            print("one->",k[x])
        elif x=="second":
            print("Two->",k[x])
        elif x=="third":
            print("Three->3")
    i=i+1
