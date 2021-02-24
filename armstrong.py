
num=int(input("enter number"))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

if(sum==num):
    print("ia arm")
else:
    print("not")

# num = int(input("Enter a number: "))  
# sum = 0  
# temp = num  
  
# while temp > 0:  
#   digit = temp % 10  
#   sum += digit ** 3  
#   temp //= 10  
  
# if num == sum:  
#   print(num,"is an Armstrong number")  
# else:  
#   print(num,"is not an Armstrong number")
    