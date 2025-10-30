time_24 = input('Enter time (24-hour format): ')
if int(time_24.split(':')[0])>=12:
    print(f'Time in 12-hour format: {str((int(time_24.split(":")[0])-12))+":"+time_24.split(":")[1]}pm')
else:
    print(f'Time in 12-hour format: {time_24}')