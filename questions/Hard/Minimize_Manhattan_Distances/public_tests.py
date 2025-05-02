from question import minimumDistance
tests = ['assert minimumDistance([[3, 10], [5, 15], [10, 2], [4, 4]]) == 12', 'assert minimumDistance([[1, 1], [1, 1], [1, 1]]) == 0']
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