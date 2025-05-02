from question import minimumDeletions
tests = ['assert minimumDeletions("aabcaba", 0) == 3', 'assert minimumDeletions("dabdcbdcdcd", 2) == 2', 'assert minimumDeletions("aaabaaa", 2) == 1']
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