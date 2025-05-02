from question import clearStars
tests = ['assert clearStars("aaba*") == "aab"', 'assert clearStars("abc") == "abc"']
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