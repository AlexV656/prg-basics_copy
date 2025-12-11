import random
def s(*args):
    print(type(args))
    print(args)
    s = 0
    for n in args:
        s+=n 
    return s 
print(s(1,2,3,4,5))

def myfunction(n1, n2):
    return n1*n2
myfunction = lambda n1,n2:n1*n2
print(myfunction(2,3))
multi = lambda number1,number2:number1*number2
sum = lambda number1,number2:number1+number2

def calc(func,n1,n2):
    return func(n1,n2)
arr = list(map(lambda n:n+10,list(range(10))))
print(arr)
arr2 = list(range(3))
arr2_copy = [x for x in arr2]
print(f'arr2 = {arr2}, arr2_copy = {arr2_copy}')
arr2 =arr2[::-1]
print(f'arr2 = {arr2}, arr2_copy = {arr2_copy}')
def f(x):
    return x*2
print(list(map(f,[1,2,3])))
def mymap(f,arr):
    for indx in range(len(arr)):
        arr[indx] = f(arr[indx])
    return arr
arr= [random.randint(0,10) for x in range(10)]
print(arr)
print([value for value in arr if value>4])