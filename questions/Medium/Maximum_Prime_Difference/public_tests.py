from question import maximumPrimeDifference
tests = ['assert maximumPrimeDifference([4, 2, 9, 5, 3]) == 3', 'assert maximumPrimeDifference([4, 8, 2, 8]) == 0']
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