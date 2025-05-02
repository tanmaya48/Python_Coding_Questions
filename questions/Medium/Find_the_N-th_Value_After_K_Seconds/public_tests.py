from question import valueAfterKSeconds
tests = ['assert valueAfterKSeconds(4, 5) == 56', 'assert valueAfterKSeconds(5, 3) == 35']
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