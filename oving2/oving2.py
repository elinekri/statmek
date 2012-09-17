#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division       # To assure that division between two integers gives a sensible result
import sys                            # Here we use the 'sys' library to handle command line arguments 
import numpy                          # A (big) library for doing array oriented numerics
import matplotlib as mpl              # A plotting framework 
from matplotlib import rc             # Configuration files
#mpl.use('PDF')                       # Uncomment to generate figures in PDF format (may not display on screen)
import matplotlib.pyplot as pyplot    # A plotting framework similar to MATLAB
#rc('text', usetex=True)               # For beautiful mathematics in figures

def make1DRandomWalkByTossingCoins(nsteps):
# Generate a one-dimensional random walk of length 'nsteps' by throwing (virtual) coins
    randomSteps = numpy.random.randint(1, 7, nsteps)
    randomWalk  = numpy.cumsum(randomSteps-7/2)
    return randomWalk


def plot2DRandomWalk(randomWalkX,randomWalkY):
# Plot a one-dimensional random walk as function of discrete time
    pyplot.plot(randomWalkX,randomWalkY,'ob')
    pyplot.xlabel(r'x $n$')
    pyplot.ylabel(r'y $X(n)$')
    pyplot.title(r'A 2-dimensional random walk')
    pyplot.show()
    # pyplot.savefig("random1DWalk")


def liste(nwalks, nsteps):
	Endpoints = numpy.zeros(nwalks)
	AbsMax = numpy.zeros(nwalks)

	for n in xrange(nwalks):         # Generates a sequence 0, 1, ... , (nwalks -1) without storing values 
	    Endpoints[n] = make1DRandomWalkByTossingCoins(nsteps)[-1] # Last entry of the returned array
	    AbsMax[n] = max(abs(make1DRandomWalkByTossingCoins(nsteps)))
	return Endpoints, AbsMax

def generateHistogramOfEndPoints(nwalks, nsteps, Endpoints):
# Decide number of bins in histogram
    nbins = int(6*numpy.sqrt(nsteps*3)+1) # Must decide size of histogram ('nbins' should be odd)
    origin = (nbins-1)/2
    histogram = numpy.zeros(nbins)   # Generates an array of 'nbins' elements, initialized with zeros 
    for n in xrange(nwalks):         # Generates a sequence 0, 1, ... , (nwalks -1) without storing values 
        bin = origin + int(Endpoints[n]) # Convert endpoint value to bin-number
        histogram[bin] +=1           
    xValues = (numpy.arange(nbins)-origin)/numpy.sqrt(nsteps)
    # numpy.arange(nbins) constructs an array [0, 1, ..., nbins-1]
    # Note how we easily can (i) subtract (or add) a constant from each element of this array,
    # (ii) divide (or multiply) each element by a constant, (iii) perform many similar operations
    pyplot.plot(xValues,histogram/nwalks, 'ob')
    pyplot.xlabel(r'Endpoint positition $x$')
    pyplot.ylabel(r'Fraction of occurences $p(x)$')
    pyplot.title(r'Histogram of endpoints for a many random walks')
    pyplot.show()
    #    pyplot.savefig("histogramOfEndpoints")
    return histogram


def generateHistogramOfMaxPoints(nwalks, nsteps, AbsMax):
# Decide number of bins in histogram
    nbins = int(6*numpy.sqrt(nsteps*6)+1) # Must decide size of histogram ('nbins' should be odd)
    origin = (nbins-1)/2
    histogram = numpy.zeros(nbins)   # Generates an array of 'nbins' elements, initialized with zeros 
    for n in xrange(nwalks):         # Generates a sequence 0, 1, ... , (nwalks -1) without storing values 
        bin = origin + int(AbsMax[n]) # Convert maxpoint value to bin-number
        histogram[bin] +=1           
    xValues = (numpy.arange(nbins)-origin)/numpy.sqrt(nsteps)
    # numpy.arange(nbins) constructs an array [0, 1, ..., nbins-1]
    # Note how we easily can (i) subtract (or add) a constant from each element of this array,
    # (ii) divide (or multiply) each element by a constant, (iii) perform many similar operations
    pyplot.plot(xValues,histogram/nwalks, 'ob')
    pyplot.xlabel(r'Maxpoint positition $x$')
    pyplot.ylabel(r'Fraction of occurences $p(x)$')
    pyplot.title(r'Histogram of maxpoints for a many random walks')
    pyplot.show()
    #    pyplot.savefig("histogramOfEndpoints")
    return maxhistogram



def main(argv):
    random1DWalkX = make1DRandomWalkByTossingCoins(5000)
    random1DWalkY = make1DRandomWalkByTossingCoins(5000)
    endp, absmax=liste(1000, 10000)
    histogram = generateHistogramOfEndPoints(1000, 10000, endp)
    maxhistogram = generateHistogramOfMaxPoints(1000, 10000, absmax)
    #plot2DRandomWalk(random1DWalkX,random1DWalkY)
    
    #pyplot.hist(endp,21)
    #pyplot.show()
    #pyplot.hist(absmax,21)
    #pyplot.show()
    #pyplot.hist(absmax,21)

if __name__ == "__main__":
    main(sys.argv[1:])


