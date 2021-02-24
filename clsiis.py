class hello:
    def __init__(self):
        self.hi()
        self.hello()
    def hi(self):
        print("we are england cricket")
        self.hello()
    def hello(self):
        print("we never give up")
class rohit(hello):
    # def __init__(self):
    def ji(self):
        super().hello()
h=rohit()

# h.hi()