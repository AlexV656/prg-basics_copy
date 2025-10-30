speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max =140
if speed_limit_max>=speed>=speed_limit_min:
    print('valid car speed')
else:
    print('Warning: invalid car speed!!')