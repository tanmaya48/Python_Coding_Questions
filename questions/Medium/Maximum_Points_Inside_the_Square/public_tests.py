from question import maxPointsInsideSquare
tests = ['assert maxPointsInsideSquare([[2, 2], [(-1), (-2)], [(-4), 4], [(-3), 1], [3, (-3)]], "abdca") == 2', 'assert maxPointsInsideSquare([[1, 1], [(-2), (-2)], [(-2), 2]], "abb") == 1', 'assert maxPointsInsideSquare([[1, 1], [(-1), (-1)], [2, (-2)]], "ccd") == 0']
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