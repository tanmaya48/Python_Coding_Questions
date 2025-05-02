from question import queryResults
tests = ['assert queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]) == [1, 2, 2, 3]', 'assert queryResults(4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]) == [1, 2, 2, 3, 4]']
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