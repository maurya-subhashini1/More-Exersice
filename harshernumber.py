def Is_harshad_number(num):
    a_digits=list(str(num1))
    sum=0
    i=1
    while i>0:
        s=1%10
        sum=sum+s
        i=i//10
    if num1%sum==0:
        print(a_digits,"harshed")
    else:
        print(a_digits,"not harshed")
num1=int(input("enter the number"))
Is_harshad_number(num1)