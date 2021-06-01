# Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke elements hone chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone chaiye. Agar humare paas yeh do lists hain:
 
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16] 
# i=0
# a=[]
# while i<len(list1):
#     s=list1[i]
#     if s  not in list2:
#         a.append(s)
#     i=i+1
# print(a)
    

#Socho aapke paas ek school ki class mein har student ke har subject ke marks hain. Jaise
 
#marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 

#Yeh ek list mein andar aur lists hain. Andar waali list mein har bache ke saare subjects mein marks hain. Ek max_marks naam ka function banao jo ki ek aisi list le aur har students ke maximum marks print kare. Jaise agar main aapke max_marks function ko upar waali list ke saath call karunga ,
 
#max_marks(marks) 

#Toh uski output yeh honi chaiye: Dekhiye ki har line har student ke maximum marks print hue hai
def max_marks(num):
    i=0
    while i<len(num):
        j=0
        k=num[i][0]
        while j<len(num[i]):
            if num[i][j]>k:
                k=num[i][j]
            j=j+1
        i=i+1
        print(k)
max_marks([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]])


    