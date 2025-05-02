from question import isArraySpecial
tests = ['assert isArraySpecial([1]) == True', 'assert isArraySpecial([2, 1, 4]) == True', 'assert isArraySpecial([4, 3, 1, 6]) == False']
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