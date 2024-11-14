s = " GAGACUU"
ww = (("A" , "U") , ("U" , "A") , ("U" , "G") , ("G" , "U") , ("C" , "G") , ("G" , "C"))
i = 1
j = 6
k = 2
def rho(i,j):
  if(s[i],s[j]) in ww:
    return 1
  else:
    return 0
while j<len(s):
  charset=j-i
  if charset>=3:
    m1=0 if len(s[i:j-1])-1 < 3 else rho(i,j-1)
    m2=0 if len(s[i+1:j-1])-1 < 3 else rho(i,j-1)
    m2=1 + m2*rho(i,j)
    m3=0 if (len(s[i:k-1])-1 + len(s[k+1:j-1])-1 ) < 3 else rho(i,j-1)
    m3=1+m3*rho(i,j)
    print("M"+str(i)+str(j), end="\t")
    print(max(m1,m2,m3))
  j+=1
  i+=1
  k+=1
