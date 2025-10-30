###
# Calculates the sum of even numbers from 1 to a given number N
#
n = int(input('Enter number: '))
sum_even = 0

# Calculate the sum of even numbers
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers from 1 to {n} is: {sum_even}")