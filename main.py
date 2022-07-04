import os
import datetime
import locale

dt = datetime.datetime.today()
print(dt.strftime("%b %d %H:%M:%S %Y")+ " +0900")
for i in range(500):
    pastdt = dt - datetime.timedelta(days=365-i)
    date = pastdt.strftime("%b %d 3:34:00 %Y")+ " +0900"
    os.system(f'echo {i} > count.txt')
    os.system('git add count.txt')
    os.system(f'git commit --allow-empty -m "{i}" --date="{date}"')
    os.system('git push origin master')