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
  for i in range(1, len(coords)-1):
    if coords[i][0] == coords[i+1][0]:
      x = coords[i][0]
      y1 = coords[i][1]
      y2 = coords[i+1][1]
      ymax = y1
      ymin = y2
      if ymax < ymin:
        ymax = y2
        ymin = y1        
      for y in range(ymin, ymax+1):
        path.append([x,y])
    if coords[i][1] == coords[i+1][1]:
      y = coords[i][1]
      x1 = coords[i][0]
      x2 = coords[i+1][0]
      xmax = x1
      xmin = x2
      if xmax < xmin:
        xmax = x2
        xmin = x1        
      for x in range(xmin, xmax+1):
        path.append([x,y])
  return path

maps = wires("03.test.txt")

path1 = set(tuple(i) for i in paths(coords(maps[0])))
path2 = set(tuple(i) for i in paths(coords(maps[1])))

intersections = path1.intersection(path2)

print(list(intersections))