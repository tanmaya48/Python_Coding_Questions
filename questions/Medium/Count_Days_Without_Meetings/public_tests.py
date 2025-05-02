from question import countDays
tests = ['assert countDays(10, [[5, 7], [1, 3], [9, 10]]) == 2', 'assert countDays(5, [[2, 4], [1, 3]]) == 1', 'assert countDays(6, [[1, 6]]) == 0']
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