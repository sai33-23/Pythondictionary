# lst1=["one","two","three"]
# lst2=[1,2,3]
# lst3 = {}
# for key in lst1:
#     for value in lst2:
#         lst3[key] = value
#         lst2.remove(value)
#         break  
# print (" dictionary is : " +  str(lst3))



# ANOTHER METHOD:




lst1=["one","two","three","four"]
lst2=[1,2,3,4]
d={}
for key in lst1:
    for value in lst2:
        d[key]=value
print(d)