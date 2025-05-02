from question import canMakeSquare
tests = ['assert canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]) == True', 'assert canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]) == False', 'assert canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]) == True']
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