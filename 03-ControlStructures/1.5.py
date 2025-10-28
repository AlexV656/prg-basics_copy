###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
test_passed = False
task_score_lst = [20, 11, 10, 9, 0]

for test_score in task_score_lst:
    if test_score>=20/2:
        test_passed=True
    if test_passed:
        print('Congratulations! You passed the test.')
    else:
        print('Unfortunately, you failed the test.')
    test_passed=False