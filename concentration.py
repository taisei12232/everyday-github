import os

for i in range(500):
    os.system(f'echo {i} > count.txt')
    os.system('git add count.txt')
    os.system(f'git commit -m "{i}"')
    os.system('git push origin master')