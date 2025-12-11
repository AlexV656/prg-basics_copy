avg_speed = lambda distance,hours,minutes:((distance*1000)/(hours*3600+minutes*60))*3.6
print(f'Average speed: {avg_speed(70,1,23)}')