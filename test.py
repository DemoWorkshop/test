import subprocess
import os

l=[]
for i in range(69):
  print(i)
  l.append(i)
print(l)
print("bye bye")


subprocess.run("git pull origin", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
