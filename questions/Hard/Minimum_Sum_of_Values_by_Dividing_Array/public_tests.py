from question import minimumValueSum
tests = ['assert minimumValueSum([1, 4, 3, 3, 2], [0, 3, 3, 2]) == 12', 'assert minimumValueSum([2, 3, 5, 7, 7, 7, 5], [0, 7, 5]) == 17', 'assert minimumValueSum([1, 2, 3, 4], [2]) == (-1)']
correct = 0
for t in tests:
    try:
        exec(t)
        correct+=1
    except:
        print('Failed Case:')
        print(t)
success = len(tests) == correct
print(correct,'/',len(tests))
print(success)