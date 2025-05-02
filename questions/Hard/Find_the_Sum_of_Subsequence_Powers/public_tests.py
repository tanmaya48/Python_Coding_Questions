from question import sumOfPowers
tests = ['assert sumOfPowers([1, 2, 3, 4], 3) == 4', 'assert sumOfPowers([2, 2], 2) == 0', 'assert sumOfPowers([4, 3, (-1)], 2) == 10']
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