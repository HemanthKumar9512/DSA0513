import matplotlib.pyplot as plt

A=[3,5,2]
B=[4,2,3]

plt.bar([1,2,3],A,label="A")
plt.bar([1,2,3],B,bottom=A,label="B")

plt.legend()
plt.show()
