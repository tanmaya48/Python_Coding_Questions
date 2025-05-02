from question import minimumTime
tests = ['assert minimumTime(3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 1, 5]) == [0, (-1), 4]', 'assert minimumTime(3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 3, 5]) == [0, 2, 3]', 'assert minimumTime(2, [[0, 1, 1]], [1, 1]) == [0, (-1)]']
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