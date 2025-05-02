from question import occurrencesOfElement
tests = ['assert occurrencesOfElement([1, 3, 1, 7], [1, 3, 2, 4], 1) == [0, (-1), 2, (-1)]', 'assert occurrencesOfElement([1, 2, 3], [10], 5) == [(-1)]']
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