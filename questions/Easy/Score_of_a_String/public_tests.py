from question import scoreOfString
tests = ['assert scoreOfString("hello") == 13', 'assert scoreOfString("zaz") == 50']
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