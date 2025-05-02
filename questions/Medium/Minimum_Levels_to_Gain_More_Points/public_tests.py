from question import minimumLevels
tests = ['assert minimumLevels([1, 0, 1, 0]) == 1', 'assert minimumLevels([1, 1, 1, 1, 1]) == 3', 'assert minimumLevels([0, 0]) == (-1)']
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