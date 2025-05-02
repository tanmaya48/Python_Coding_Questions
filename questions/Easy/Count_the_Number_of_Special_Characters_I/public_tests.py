from question import numberOfSpecialChars
tests = ['assert numberOfSpecialChars("aaAbcBC") == 3', 'assert numberOfSpecialChars("abc") == 0', 'assert numberOfSpecialChars("abBCab") == 1']
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