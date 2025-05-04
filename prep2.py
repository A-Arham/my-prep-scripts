import re
# def solution(array_a, array_b):
#     err=[]
#     s=0
#     l1=len(array_a)
#     l2=len(array_b)
#     m=max(l1,l2)

#     for i in range(m):
#         err.append((abs(array_a[i]-array_b[i]))*(abs(array_a[i]-array_b[i])))
    
#     s=sum(err)
#     s=s/len(err)
#     return s


# b1 = [10, 20, 10, 2]
# b2 = [10, 25, 5, -2]
# solution(b1,b2)


# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
            
# def to_camel_case(text):

#     intt=list(text)
#     if not intt:
#         return text
#     else:
#         dd = text.replace('_', '-').split('-')
#         d=len(dd)
#         txt=""
#         out=[]
#         for i in range (d):
#             txt=dd[i]
#             txt=str(txt)
#             if(i==0):
#                 lst=list(txt)
#                 chck=lst[i]
#                 chck=str(chck)
#                 capflag=chck.isupper()
#                 if(capflag==True):
#                     txt=txt.capitalize()
#                     out.append(txt)
#                 else:
#                     out.append(txt)
#             else:
#                 txt=txt.capitalize()
#                 out.append(txt)
#         output=''.join(out)
#         #print(output)
#     return output
    
    
    

# print(to_camel_case("the_stealth_warrior"))


