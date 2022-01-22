my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
max=0
sec=0
for i  in my_dict:
    if max<my_dict[i]:
        max=my_dict[i]
        print(max)
    elif sec<my_dict[i]:
        print(sec)
    else:
        print("third")
