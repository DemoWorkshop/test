import subprocess
import os

subprocess.run("git pull origin", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

l=[]
for i in range(69):
  print(i)
  l.append(i)
print(l)
print("bye bye")
