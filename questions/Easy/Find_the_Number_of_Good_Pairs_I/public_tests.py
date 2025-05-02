from question import numberOfPairs
tests = ['assert numberOfPairs([1, 3, 4], [1, 3, 4], 1) == 5', 'assert numberOfPairs([1, 2, 4, 12], [2, 4], 3) == 2']
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