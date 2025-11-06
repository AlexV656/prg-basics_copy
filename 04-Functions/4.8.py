def time_string(hours,minutees,time_format):
    if time_format=='24':
        return f'{hours}:{minutees}'
    
    elif hours>=12:
        return f'{hours-12}:{minutees}pm'
    else:
        return f'{hours}:{minutees}am'
print(time_string(19,15,'24'))