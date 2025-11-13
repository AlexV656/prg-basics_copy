def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n]
lst_check = [1,4,7]
for value in lst_check:
    print(weekday(value))