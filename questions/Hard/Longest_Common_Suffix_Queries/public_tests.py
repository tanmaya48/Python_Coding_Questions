from question import stringIndices
tests = ['assert stringIndices(["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"]) == [1, 1, 1]', 'assert stringIndices(["abcdefgh", "poiuygh", "ghghgh"], ["gh", "acbfgh", "acbfegh"]) == [2, 0, 2]']
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