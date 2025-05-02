from question import maximumTotalDamage
tests = ['assert maximumTotalDamage([1, 1, 3, 4]) == 6', 'assert maximumTotalDamage([7, 1, 6, 6]) == 13']
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