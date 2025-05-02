from question import findAnswer
tests = ['assert findAnswer(6, [[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]]) == [True, True, True, False, True, True, True, False]', 'assert findAnswer(4, [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]) == [True, False, False, True]']
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