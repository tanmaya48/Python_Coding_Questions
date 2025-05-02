from question import isValid
tests = ['assert isValid("234Adas") == True', 'assert isValid("b3") == False', 'assert isValid("a3$e") == False']
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