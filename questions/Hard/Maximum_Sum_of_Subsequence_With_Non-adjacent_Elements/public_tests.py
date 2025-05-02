from question import maximumSumSubsequence
tests = ['assert maximumSumSubsequence([3, 5, 9], [[1, (-2)], [0, (-3)]]) == 21', 'assert maximumSumSubsequence([0, (-1)], [[0, (-5)]]) == 0']
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