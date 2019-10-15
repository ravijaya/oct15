import subprocess

op = subprocess.check_output(['ifconfig'])
print(op.decode())  # bytes into str