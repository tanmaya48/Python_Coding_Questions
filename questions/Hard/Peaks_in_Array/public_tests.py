from question import countOfPeaks
tests = ['assert countOfPeaks([3, 1, 4, 2, 5], [[2, 3, 4], [1, 0, 4]]) == [0]', 'assert countOfPeaks([4, 1, 4, 2, 1, 5], [[2, 2, 4], [1, 0, 2], [1, 0, 4]]) == [0, 1]']
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