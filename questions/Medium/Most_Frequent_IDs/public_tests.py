from question import mostFrequentIDs
tests = ['assert mostFrequentIDs([2, 3, 2, 1], [3, 2, (-3), 1]) == [3, 3, 2, 2]', 'assert mostFrequentIDs([5, 5, 3], [2, (-2), 1]) == [2, 0, 1]']
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