from question import minCostToEqualizeArray
tests = ['assert minCostToEqualizeArray([4, 1], 5, 2) == 15', 'assert minCostToEqualizeArray([2, 3, 3, 3, 5], 2, 1) == 6', 'assert minCostToEqualizeArray([3, 5, 3], 1, 3) == 4']
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