from question import duplicateNumbersXOR
tests = ['assert duplicateNumbersXOR([1, 2, 1, 3]) == 1', 'assert duplicateNumbersXOR([1, 2, 3]) == 0', 'assert duplicateNumbersXOR([1, 2, 2, 1]) == 3']
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