from question import minAnagramLength
tests = ['assert minAnagramLength("abba") == 2', 'assert minAnagramLength("cdef") == 4']
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