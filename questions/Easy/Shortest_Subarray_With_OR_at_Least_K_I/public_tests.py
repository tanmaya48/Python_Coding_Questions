from question import minimumSubarrayLength
tests = ['assert minimumSubarrayLength([1, 2, 3], 2) == 1', 'assert minimumSubarrayLength([2, 1, 8], 10) == 3', 'assert minimumSubarrayLength([1, 2], 0) == 1']
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