from question import numberOfStableArrays
tests = ['assert numberOfStableArrays(1, 1, 2) == 2', 'assert numberOfStableArrays(1, 2, 1) == 1', 'assert numberOfStableArrays(3, 3, 2) == 14']
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