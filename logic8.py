# Write a Python program to print a dictionary line by line



students = {'sai':{'class':'V','rolld_id':2},'jyoti':{'class':'V','roll_id':3}}
for a in students:
    print(a)
    for b in students[a]:
        print (b,':',students[a][b])
