from question import numberOfChild
tests = ['assert numberOfChild(3, 5) == 1', 'assert numberOfChild(5, 6) == 2', 'assert numberOfChild(4, 2) == 2']
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