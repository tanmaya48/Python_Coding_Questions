from question import compressedString
tests = ['assert compressedString("abcde") == "1a1b1c1d1e"', 'assert compressedString("aaaaaaaaaaaaaabb") == "9a5a2b"']
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