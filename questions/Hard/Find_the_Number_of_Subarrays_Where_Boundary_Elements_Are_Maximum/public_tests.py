from question import numberOfSubarrays
tests = ['assert numberOfSubarrays([1, 4, 3, 3, 2]) == 6', 'assert numberOfSubarrays([3, 3, 3]) == 6', 'assert numberOfSubarrays([1]) == 1']
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