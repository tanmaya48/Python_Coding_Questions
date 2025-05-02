from question import clearDigits
tests = ['assert clearDigits("abc") == "abc"', 'assert clearDigits("cb34") == ""']
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