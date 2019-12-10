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

def paths(coords):
  path = []
  for i in range(len(coords)-1):
    if coords[i][0] == coords[i+1][0]:
      x = coords[i][0]
      y1 = coords[i][1]
      y2 = coords[i+1][1]
      inc = 1
      if y1 > y2:
        inc = -1
      for y in range(y1, y2, inc):
        path.append([x,y])
    else:
      y = coords[i][1]
      x1 = coords[i][0]
      x2 = coords[i+1][0]
      inc = 1
      if x1 > x2:
        inc = -1
      for x in range(x1, x2, inc):
        path.append([x,y])
  return path

maps = wires("03.txt")

path1 = map(tuple, paths(coords(maps[0])))
path2 = map(tuple, paths(coords(maps[1])))

intersections = list(set(path1).intersection(set(path2)))
intersections.remove((0,0))

print(min([path1.index(i) + path2.index(i) for i in intersections]) )