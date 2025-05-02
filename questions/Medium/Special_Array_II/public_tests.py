from question import isArraySpecial
tests = ['assert isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]) == [False]', 'assert isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]) == [False, True]']
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