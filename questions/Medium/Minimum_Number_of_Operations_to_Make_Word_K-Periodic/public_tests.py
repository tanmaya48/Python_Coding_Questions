from question import minimumOperationsToMakeKPeriodic
tests = ['assert minimumOperationsToMakeKPeriodic("leetcodeleet", 4) == 1', 'assert minimumOperationsToMakeKPeriodic("leetcoleet", 2) == 3']
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