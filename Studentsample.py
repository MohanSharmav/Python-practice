marks=[]
sum=0
for i in range(2):
    n=input("enter student marks")
    marks.append(n)
print(marks)
# marks=[10,50]
p=sum()
print(p)
# op=sum(marks)
# print(op)
lenn=len(marks)
for x in marks:
    print("look",x)
    x=int(x)
    if x>90:
        print("90")
    elif (x>70 and x<90):
        print("70")

y=sum(marks)
