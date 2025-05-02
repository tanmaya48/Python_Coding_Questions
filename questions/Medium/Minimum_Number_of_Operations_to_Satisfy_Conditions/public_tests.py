from question import minimumOperations
tests = ['assert minimumOperations([[1, 0, 2], [1, 0, 2]]) == 0', 'assert minimumOperations([[1, 1, 1], [0, 0, 0]]) == 3', 'assert minimumOperations([[1], [2], [3]]) == 2']
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