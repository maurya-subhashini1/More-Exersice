# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain. Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye. Jaise:
 
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
i=0
s=[]
while i<len(string_list):
    b=string_list[i]
    if b not in s:
        s.append(b)
    i=i+1
print(s)