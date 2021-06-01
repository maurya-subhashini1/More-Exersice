# def break_into_words(sentence):
#     a=sentence.split()
#     pntence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
# break_into_words(sentence)
# rint(a)


# def string_reverse(str1):
#     num1=''
#     i=len(str1)
#     while i>0:
#         num1+=str1[i-1]
#         i=i-1
#     return num1    
# print(string_reverse('345maurya'))


def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))




