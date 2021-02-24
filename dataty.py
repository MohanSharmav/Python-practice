li=['hi','hello',5,6]
print(li)
print(id(li))
li.append('Sharma')
print(li)
print(id(li))

print(len(li))
li.insert(1,9)
print("new list : ",li)
x=['new one']
li.extend(x)
print(li)
p=li[0]
print(p)