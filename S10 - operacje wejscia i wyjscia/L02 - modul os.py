import os
import time

dir = input()

if not os.path.isdir(dir):
    print("NO NO NO")
else:
    file = input()
    path = os.path.join(dir, file)
    if not os.path.isfile(path):
        print("NO NO NO")
    else:
        print(time.localtime(os.path.getmtime(path)))
        print(os.path.getsize(path))
        print(os.getcwd())
        print(os.path.relpath(path))
        
