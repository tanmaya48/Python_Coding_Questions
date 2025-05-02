from question import findWinningPlayer
tests = ['assert findWinningPlayer([4, 2, 6, 3, 9], 2) == 2', 'assert findWinningPlayer([2, 5, 4], 3) == 1']
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