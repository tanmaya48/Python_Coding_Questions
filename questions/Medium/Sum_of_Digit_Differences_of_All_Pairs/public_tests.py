from question import sumDigitDifferences
tests = ['assert sumDigitDifferences([13, 23, 12]) == 4', 'assert sumDigitDifferences([10, 10, 10, 10]) == 0']
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