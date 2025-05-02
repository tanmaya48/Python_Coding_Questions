from question import numberOfRightTriangles
tests = ['assert numberOfRightTriangles([[0, 1, 0], [0, 1, 1], [0, 1, 0]]) == 2', 'assert numberOfRightTriangles([[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]) == 0', 'assert numberOfRightTriangles([[1, 0, 1], [1, 0, 0], [1, 0, 0]]) == 2']
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