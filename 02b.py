def split(file, delim):
  f = open(file, "r")
  return [int(x.strip()) for x in f.read().split(delim)]

def process(ops, noun, verb):
  newOps = ops[:]
  newOps[1] = noun
  newOps[2] = verb
  for i in range(0, len(newOps), 4):
    x = newOps[i]
    if x in [1,2]:
      a = newOps[i+1]
      b = newOps[i+2]
      c = newOps[i+3]
      if x == 1:
        newOps[c] = newOps[a] + newOps[b]
      if x == 2:
        newOps[c] = newOps[a] * newOps[b]
    if x == 99:
      break
  return newOps

ops = split("02.txt", ",")

for i in range(100):
  for j in range(100):
    if process(ops, i, j)[0] == 19690720:
      print(str(i)+str(j))
      break