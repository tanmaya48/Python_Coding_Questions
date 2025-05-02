from question import medianOfUniquenessArray
tests = ['assert medianOfUniquenessArray([1, 2, 3]) == 1', 'assert medianOfUniquenessArray([3, 4, 3, 4, 5]) == 2', 'assert medianOfUniquenessArray([4, 3, 5, 4]) == 2']
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