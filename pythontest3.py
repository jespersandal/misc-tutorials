import numpy
import pylab
import math

t = numpy.linspace(0,6,100)
r = t * 1.1
y = numpy.exp(r)
b = -1 * (t * 2.5)
q = numpy.exp(b)
k =  400 / ((1 + 300*q)**0.8)
z = t + 2.5

pylab.plot(t,y,'-r')
pylab.plot(z,k,'-g')
pylab.show()
