min = 136818
max = 685979

def ascending(x):
  x = str(x)
  for i in range(0, len(x)-1):
    if int(x[i]) > int(x[i+1]):
      return False
  return True

def repeats(x):
  x = str(x)
  for i in range(0, len(x)):
    if x.count(x[i]) > 1:
      return True
  return False

def validate(x):
  x = str(x)
  return repeats(x) and ascending(x)

count = 0
for i in range(min, max+1):
  if validate(i):
    count += 1

print(count)