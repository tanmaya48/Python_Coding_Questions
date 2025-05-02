from question import minimumMoves
tests = ['assert minimumMoves([1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 3, 1) == 3', 'assert minimumMoves([0, 0, 0, 0], 2, 3) == 4']
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