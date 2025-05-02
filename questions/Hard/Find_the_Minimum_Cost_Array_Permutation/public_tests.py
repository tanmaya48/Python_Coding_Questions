from question import findPermutation
tests = ['assert findPermutation([1, 0, 2]) == [0, 1, 2]', 'assert findPermutation([0, 2, 1]) == [0, 2, 1]']
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