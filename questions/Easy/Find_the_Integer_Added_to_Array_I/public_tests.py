from question import addedInteger
tests = ['assert addedInteger([2, 6, 4], [9, 7, 5]) == 3', 'assert addedInteger([10], [5]) == (-5)', 'assert addedInteger([1, 1, 1, 1], [1, 1, 1, 1]) == 0']
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