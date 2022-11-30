musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print('influenza')
else:
    print('flu unlikely')

if musclePain and fever and weakness:
    print('influenza')
elif weakness and(not musclePain or not fever):
    print('rest')
else:
    print('you may be cold')
    
isMan = True

if musclePain and fever and weakness:
    print('influenza')
elif isMan and (musclePain or fever or weakness):
    print('influenza')
elif weakness and(not musclePain or not fever):
    print('rest')
else:
    print('you may be cold')

isCheckCompleted = True

print('CHECK COMPLETED' if isCheckCompleted else 'CHECK NOT COMPLETED')

isCheckCompleted = False

print('CHECK COMPLETED' if isCheckCompleted else 'CHECK NOT COMPLETED')