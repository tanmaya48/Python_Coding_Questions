from question import findKthSmallest
tests = ['assert findKthSmallest([3, 6, 9], 3) == 9', 'assert findKthSmallest([5, 2], 7) == 12']
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