import os
import uuid
import sys

for i in range(int(sys.argv[1])):
    id = uuid.uuid4()
    os.system(f'echo {id} > count.txt')
    os.system('git add count.txt')
    os.system(f'git commit -m "{id}"')
    os.system('git push origin master')
