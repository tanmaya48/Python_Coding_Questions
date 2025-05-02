from question import getResults
tests = ['assert getResults([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]) == [False, True, True]', 'assert getResults([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]) == [True, True, False]']
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