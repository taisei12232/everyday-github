import os
import datetime
import locale
import uuid
import subprocess

dt = datetime.datetime.today()
print(dt.strftime("%b %d %H:%M:%S %Y")+ " +0900")
for i in range(365):
    id = uuid.uuid4()
    pastdt = dt - datetime.timedelta(days=365-i)
    date = pastdt.strftime("%b %d 3:34:00 %Y")+ " +0900"
    subprocess.run(f'echo {id} > count.txt', shell=True)
    subprocess.run(f'git add count.txt', shell=True)
    subprocess.run(f'git commit --allow-empty -m "{id}" --date="{date}"', shell=True)
subprocess.run(f'git push origin master', shell=True)
