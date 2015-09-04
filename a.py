import subprocess

proc = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
(out,err)=proc.communicate()
print out

