def wires(file):
  f = open(file, "r")
  return [[item.strip() for item in line.split(",")] for line in f.readlines()]

def coords(directions):
  coords = [[0,0]]
  x = 0
  y = 0
  for dir in directions:
    cardinal = dir[0]
    distance = int(dir[1:])
    if cardinal == "U":
      y += distance
    if cardinal == "R":
      x += distance
    if cardinal == "L":
      x -= distance
    if cardinal  == "D": 
      y -= distance
    coords.append([x,y])
  return coords

maps = wires("03.test.txt")

print(coords(wires("03.test.txt")[0]))