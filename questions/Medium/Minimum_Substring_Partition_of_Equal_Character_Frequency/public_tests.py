from question import minimumSubstringsInPartition
tests = ['assert minimumSubstringsInPartition("fabccddg") == 3', 'assert minimumSubstringsInPartition("abababaccddb") == 2']
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