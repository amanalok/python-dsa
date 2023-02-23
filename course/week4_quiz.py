def mystery(l):
  if (l == []):
    return(l)
  else:
    mid = len(l)//2
    if (len(l)%2 == 0):
      return l[mid-1:mid+1] + mystery(l[:mid-1]+l[mid+1:])
    else:
      return l[mid:mid+1] + mystery(l[:mid]+l[mid+1:])
    
print(mystery([22,14,19,65,82,55]))

triples = [ (x,y,z) for x in range(1,4) for y in range(2,5) for z in range(5,8) if x+y > z ]
print(triples)

actor = {}
actor["Star Wars"] = ["Rey","Ridley"]
actor["Star Wars, Rey"] = "Ridley"
actor[("Star Wars", "Rey")] = "Ridley"