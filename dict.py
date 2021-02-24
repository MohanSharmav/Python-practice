d={1:"hello",2:"bye",3:['hi','how ']}
print(d)
x=d[1]
print(x)
p=d.get("hello")
print(p)
print(d.values())
print(d.keys())
d[1]="hero"
print(d)
d.update({1:"look"})
print(d)