def door_det(detector):
    people_in = 0
    for x in detector:
        if x=='+':people_in+=1
        else: people_in-=1
        if people_in>=3:return True
    return False
        
print(door_det("+-+++-+---"))
print(door_det("+-+-+-+-"))

print(door_det("+-++-+--"))

print(door_det("+-++-++-+---"))
