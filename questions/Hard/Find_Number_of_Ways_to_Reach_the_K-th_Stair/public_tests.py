from question import waysToReachStair
tests = ['assert waysToReachStair(0) == 2', 'assert waysToReachStair(1) == 4']
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