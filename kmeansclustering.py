import math
dp=((1,1),(2,1),(4,3),(5,4))
cent=((1,1),(2,1))
print("\t",cent,"ASSIGNED")
for i in dp:
  a,b=i
  print(i,end="")
  l1=[]
  for j in cent:
    c,d=j
    print(end="\t")
    dist=((a-c)**2+(b-d)**2)
    ed=round(math.sqrt(dist),2)
    print(ed,end="\t")
    l1.append(ed)
  m=min(l1)
  minc=l1.index(m)
  print(minc,end="\t")
  print()