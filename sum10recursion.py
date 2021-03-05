def hello(n):
    if(n==0):
        return 0
    else:
        return n+hello(n-1)
        
hello(10)