import os
import sys


# find files
log_files = []
for path, subdirs, files in os.walk('logs'):
    for name in files:
        if name.endswith('.log'):
            log_file = os.path.join(path, name)
            log_files.append(log_file)

# file selection
if len(log_files) == 0:
    print('No .log file found')
    sys.exit(1)
elif len(log_files) == 1:
    log_file = log_files[0]
else:
    for i, log_file in log_files:
        print(f'({i}) {log_file}')
    i = int(input('Select one: '))
    log_file = log_files[i]
print(log_file)

# analyze
set_ns = set()
with open(log_file) as file:
    for line in file:
        if line.startswith('solver:PROFILE'):
            line = line.strip()
            tokens = line.split()

            n = int(tokens[1].split(':')[-1])
            set_ns.add(n)

print(set_ns)