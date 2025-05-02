from question import countAlternatingSubarrays
tests = ['assert countAlternatingSubarrays([0, 1, 1, 1]) == 5', 'assert countAlternatingSubarrays([1, 0, 1, 0]) == 10']
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