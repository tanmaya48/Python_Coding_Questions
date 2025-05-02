from question import minimumDifference
tests = ['assert minimumDifference([1, 2, 4, 5], 3) == 0', 'assert minimumDifference([1, 3, 1, 3], 2) == 1', 'assert minimumDifference([1], 10) == 9']
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