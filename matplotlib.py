seq="ATCCGGCTCGAATTCGAGGTAAAG"
for i in range (len(seq)):
  a=seq.count("A")
  b=seq.count("T")
  c=seq.count("C")
  d=seq.count("G")

import matplotlib.pyplot as plt
plt.title("Dna graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

x=["A","T","C","G"]      #line graph
y=[a,b,c,d]


plt.bar(x,y)
plt.show()