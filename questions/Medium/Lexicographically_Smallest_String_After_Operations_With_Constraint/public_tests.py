from question import getSmallestString
tests = ['assert getSmallestString("zbbz", 3) == "aaaz"', 'assert getSmallestString("xaxcd", 4) == "aawcd"', 'assert getSmallestString("lol", 0) == "lol"']
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