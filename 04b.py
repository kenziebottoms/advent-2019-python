min = 136818
max = 685979

def ascending(x):
  x = str(x)
  for i in range(0, len(x)-1):
    if int(x[i]) > int(x[i+1]):
      return False
  return True

def streaks(x):
  x = str(x)
  streaks = []
  count = 1
  for i in range(0, len(x)-1):
    if x[i] == x[i+1]:
      count += 1
    else:
      streaks.append(count)
      count = 1
  streaks.append(count)
  return streaks

def validate(x):
  x = str(x)
  return 2 in streaks(x) and ascending(x)

count = 0
for i in range(min, max+1):
  if validate(i):
    count += 1

print(count)