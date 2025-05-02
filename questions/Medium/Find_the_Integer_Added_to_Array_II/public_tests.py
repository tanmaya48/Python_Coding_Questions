from question import minimumAddedInteger
tests = ['assert minimumAddedInteger([4, 20, 16, 12, 8], [14, 18, 10]) == (-2)', 'assert minimumAddedInteger([3, 5, 5, 3], [7, 7]) == 2']
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