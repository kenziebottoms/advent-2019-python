def lines(file):
  lines = []
  f = open(file, "r")
  for line in f:
    lines.append(line.strip())
  return lines

def fuel(mass):
  return int(int(mass)/3) - 2

print(sum(map(fuel, lines("01.txt"))))