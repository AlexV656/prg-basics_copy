class Prog():
    def __init__(self,n):
        self.x = 0
        self.last_val = 10
    def __next__(self):
        if self.x<self.last_val:
            self.x+=1 
            return self.x
        raise StopIteration 
        
    def __iter__(self):
        return self
print(type(range(10)))
def rec(n):
    for x in range(n):
        yield x
print(type(rec(10)))
for x in Prog(10):
    print(x)