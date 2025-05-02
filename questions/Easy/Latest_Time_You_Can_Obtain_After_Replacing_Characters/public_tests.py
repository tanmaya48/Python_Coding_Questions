from question import findLatestTime
tests = ['assert findLatestTime("1?:?4") == "11:54"', 'assert findLatestTime("0?:5?") == "09:59"']
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