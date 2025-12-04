class Person():
    def __init__(self):
        self.x = 10
    def __str__(self):
        return 'string function'
    def __int__(self):
        return 1 
p = Person()
print( int(p) )
print(str(p))
