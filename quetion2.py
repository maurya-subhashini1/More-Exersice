def squares_no(num):
    key=1
    dict1={}
    while key<=num:
        value=key**2
        dict1[key]=value
        key=key+1
    return(dict1)
a=int(input("enter the number:"))
print(squares_no(a))




