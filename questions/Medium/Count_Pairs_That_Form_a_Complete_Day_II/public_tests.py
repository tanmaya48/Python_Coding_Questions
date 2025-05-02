from question import countCompleteDayPairs
tests = ['assert countCompleteDayPairs([12, 12, 30, 24, 24]) == 2', 'assert countCompleteDayPairs([72, 48, 24, 3]) == 3']
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