from question import maximumEnergy
tests = ['assert maximumEnergy([5, 2, (-10), (-5), 1], 3) == 3', 'assert maximumEnergy([(-2), (-3), (-1)], 2) == (-1)']
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