s1="ATA"
s2="AAA"
s3="ATT"
s4="ATT"

def calculation(ll):
  mydict={"A":0,"T":0,"C":0,"G":0}
  for i in li:
    if i in mydict:
      mydict[i]=mydict[i]+1
  if mydict[i]>len(li)/2:
    v = list(mydict.values())
    k = list(mydict.keys())
    print(k[v.index(max(v))],max(mydict.values()))
  elif mydict[i]==len(li)/2:
    print("*")



for i in range(len(s1)):
  li=[]

  li.append(s1[i])
  li.append(s2[i])
  li.append(s3[i])
  li.append(s4[i])
  print(li)
  calculation(li)