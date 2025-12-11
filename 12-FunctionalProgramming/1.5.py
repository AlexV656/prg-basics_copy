def avg_speed(distance,hours,minutes):
    return ((distance*1000)/(hours*3600+minutes*60))*3.6
# distance = int(input('Enter distance in km: '))
# hours = int(input('Enter number of travel hours: '))
# minutes = int(input('Enter number of travel minutes'))
print(f'Average speed: {avg_speed(70,1,23)}')