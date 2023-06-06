import subprocess
import os

subprocess.run("git pull origin", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
for i in range(5):
  print(i, "hey")
print("bye bye")
