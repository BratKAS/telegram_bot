import os
import subprocess

dp = os.path.expanduser("~/Desktop")

contents = os.listdir(dp)

tn = 'вопрос.txt'
tp = os.path.join(dp, tn)
with open(tp, 'w') as file:
    file.write('Кто я?')

subprocess.Popen(['open', tp])
