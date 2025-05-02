from question import isSubstringPresent
tests = ['assert isSubstringPresent("leetcode") == True', 'assert isSubstringPresent("abcba") == True', 'assert isSubstringPresent("abcd") == False']
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