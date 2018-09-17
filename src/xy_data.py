import numpy as np
import pylab as py

infile = open("../data/xy.dat","r")

x = []
y = []
for line in infile:
  x_, y_ = [float(w) for w in infile.split()]
  x.append(x_)
  y.append(y_)

infile.close()

x = np.array(x)
y = np.array(y)

pl.plot(x,y)
pl.show()
