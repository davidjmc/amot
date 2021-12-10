env = {}
with open('env.ini', 'r') as f:
  for line in f:
    if line.strip() == '':
      continue
    [key, val] = [p.strip() for p in line.split('=')]
    env[key] = val

# del key
# del val
# del line
# del f

print(env['THING_ID'])

input()