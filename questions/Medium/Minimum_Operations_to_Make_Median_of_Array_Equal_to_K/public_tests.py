from question import minOperationsToMakeMedianK
tests = ['assert minOperationsToMakeMedianK([2, 5, 6, 8, 5], 4) == 2', 'assert minOperationsToMakeMedianK([2, 5, 6, 8, 5], 7) == 3', 'assert minOperationsToMakeMedianK([1, 2, 3, 4, 5, 6], 4) == 0']
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