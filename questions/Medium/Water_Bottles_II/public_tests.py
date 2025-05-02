from question import maxBottlesDrunk
tests = ['assert maxBottlesDrunk(13, 6) == 15', 'assert maxBottlesDrunk(10, 3) == 13']
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