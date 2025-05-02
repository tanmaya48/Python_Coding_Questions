from question import satisfiesConditions
tests = ['assert satisfiesConditions([[1, 0, 2], [1, 0, 2]]) == True', 'assert satisfiesConditions([[1, 1, 1], [0, 0, 0]]) == False', 'assert satisfiesConditions([[1], [2], [3]]) == False']
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