from question import maxTotalReward
tests = ['assert maxTotalReward([1, 1, 3, 3]) == 4', 'assert maxTotalReward([1, 6, 4, 3, 2]) == 11']
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