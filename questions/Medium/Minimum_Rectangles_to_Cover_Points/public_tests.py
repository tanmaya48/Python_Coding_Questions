from question import minRectanglesToCoverPoints
tests = ['assert minRectanglesToCoverPoints([[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], 1) == 2', 'assert minRectanglesToCoverPoints([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], 2) == 3', 'assert minRectanglesToCoverPoints([[2, 3], [1, 2]], 0) == 2']
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