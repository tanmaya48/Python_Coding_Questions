from question import longestMonotonicSubarray
tests = ['assert longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2', 'assert longestMonotonicSubarray([3, 3, 3, 3]) == 1', 'assert longestMonotonicSubarray([3, 2, 1]) == 3']
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