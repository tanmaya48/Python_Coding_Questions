from question import maximumLengthSubstring
tests = ['assert maximumLengthSubstring("bcbbbcba") == 4', 'assert maximumLengthSubstring("aaaa") == 2']
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