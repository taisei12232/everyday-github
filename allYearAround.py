import os
import datetime
import locale
import uuid

dt = datetime.datetime.today()
print(dt.strftime("%b %d %H:%M:%S %Y")+ " +0900")
for i in range(365):
    id = uuid.uuid4()
    pastdt = dt - datetime.timedelta(days=365-i)
    date = pastdt.strftime("%b %d 3:34:00 %Y")+ " +0900"
    os.system(f'echo {id} > count.txt')
    os.system('git add count.txt')
    os.system(f'git commit --allow-empty -m "{id}" --date="{date}"')
    os.system('git push origin master')
