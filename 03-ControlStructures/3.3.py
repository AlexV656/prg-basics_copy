###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age_lst = [72,65,64,18,17]
for age in age_lst:
    if age < 18 or age>=65 :
        print('discount')
    else:
        print('no discount')