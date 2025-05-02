from question import minimumChairs
tests = ['assert minimumChairs("EEEEEEE") == 7', 'assert minimumChairs("ELELEEL") == 2', 'assert minimumChairs("ELEELEELLL") == 3']
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