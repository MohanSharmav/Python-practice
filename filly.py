# l=[1,2,3]
# def de(p):
#     if(p>10):
#         return True
#     else:
#         return False
# x=filter(de,l)
# print(list(x))

l=[1,2,4,5]
x=filter(lambda x:x==2,l)
print(list(x))