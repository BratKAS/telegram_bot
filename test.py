import os
import subprocess

dp = os.path.expanduser("~/Desktop")

tn = 'hi.txt'
tp = os.path.join(dp, tn)
with open(tp, 'w') as file:
    file.write('Hi!')

subprocess.Popen(['open', tp])
