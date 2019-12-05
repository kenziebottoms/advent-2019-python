def lines(file):
  lines = []
  f = open(file, "r")
  for line in f:
    lines.append(line.strip())
  return lines

def fuel(mass):
  return int(int(mass)/3) - 2

def fuel_of_fuel(mass):
  total = 0
  while fuel(mass) >= 0:
    total += fuel(mass)
    mass = fuel(mass)
  return total

print(sum(map(fuel_of_fuel, lines("01.txt"))))