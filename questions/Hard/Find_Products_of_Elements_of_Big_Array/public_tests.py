from question import findProductsOfElements
tests = ['assert findProductsOfElements([[1, 3, 7]]) == [4]', 'assert findProductsOfElements([[2, 5, 3], [7, 7, 4]]) == [2, 2]']
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