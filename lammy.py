def myfunc(n):
  return lambda a : a * n
l=[1,2,3]
x=map(myfunc,l)
print(list(x))
# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

# print(x)

# #convert the map into a list, for readability:
# print(list(x))
