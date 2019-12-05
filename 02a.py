def split(file, delim):
  f = open(file, "r")
  return [int(x.strip()) for x in f.read().split(delim)]

