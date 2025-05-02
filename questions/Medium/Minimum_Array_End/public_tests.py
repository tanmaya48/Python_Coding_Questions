from question import minEnd
tests = ['assert minEnd(3, 4) == 6', 'assert minEnd(2, 7) == 15']
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