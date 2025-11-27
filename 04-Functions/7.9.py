def dig_sum(number,even):
    if even: return sum([int(dig) for dig in str(number) if int(dig)%2==0])
    else:return sum([int(dig) for dig in str(number) if int(dig)%2==1])
if __name__=="__main__":
    for x in [(3124,True),(3124,False),(20576,False),(20576,True),(13115,True)]:
        print(dig_sum(x[0],x[1]))
