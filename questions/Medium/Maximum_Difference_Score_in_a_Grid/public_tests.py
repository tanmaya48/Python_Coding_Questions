from question import maxScore
tests = ['assert maxScore([[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]) == 9', 'assert maxScore([[4, 3, 2], [3, 2, 1]]) == (-1)']
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