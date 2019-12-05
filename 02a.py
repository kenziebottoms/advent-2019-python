def split(file, delim):
  f = open(file, "r")
  return [int(x.strip()) for x in f.read().split(delim)]

def process(ops):
  for i in range(0, len(ops), 4):
    x = ops[i]
    if x in [1,2]:
      a = ops[i+1]
      b = ops[i+2]
      c = ops[i+3]
      if x == 1:
        ops[c] = ops[a] + ops[b]
      if x == 2:
        ops[c] = ops[a] * ops[b]
    if x == 99:
      break
  return ops

ops = split("02.txt", ",")

ops[1] = 12
ops[2] = 2

print(process(ops))