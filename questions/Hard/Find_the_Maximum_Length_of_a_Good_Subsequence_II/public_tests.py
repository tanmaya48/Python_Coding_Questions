from question import maximumLength
tests = ['assert maximumLength([1, 2, 1, 1, 3], 2) == 4', 'assert maximumLength([1, 2, 3, 4, 5, 1], 0) == 2']
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