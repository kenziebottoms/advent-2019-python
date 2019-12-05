def split(file, delim):
  f = open(file, "r")
  return map(str.strip, f.read().split(delim))

def ops(list):
  ops = [[]]
  separators = [1,2,99]
  i = -1
  for item in list:
    if int(item) in separators:
      i += 1
      ops.append([])
    ops[i].append(int(item))
  return ops

for line in ops(split("02.txt",",")):
  print(line)