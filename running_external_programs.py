from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob



command = "netstat -n"

command_words = shlex.split(command)

run(command_words)   # works on all platforms
print('-' * 60)

try:
    process = run(command_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err)
else:
    output = process.stdout.decode()  # convert output from bytes to text
    print(output[:100])
print('-' * 60)
lines = output.splitlines()  # split output into lines
established_connections = [line for line in lines if 'ESTABLISHED' in line]
print(len(established_connections))

