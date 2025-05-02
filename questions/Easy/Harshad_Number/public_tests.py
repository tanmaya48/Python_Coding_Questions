from question import sumOfTheDigitsOfHarshadNumber
tests = ['assert sumOfTheDigitsOfHarshadNumber(18) == 9', 'assert sumOfTheDigitsOfHarshadNumber(23) == (-1)']
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