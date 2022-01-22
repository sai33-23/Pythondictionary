d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=d.sorted(values())
for x in d:
    for y in d:
        if d[x]>d[y]:
            d[x],d[y]=d[y],d[x]
print(d)