from question import countSubstrings
tests = ['assert countSubstrings("abada", "a") == 6', 'assert countSubstrings("zzz", "z") == 6']
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