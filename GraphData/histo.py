import numpy as np
import matplotlib.pyplot as plt#, mpld3

#data = np.array([.05, .32, .44, .68, .62, .56, .81, .36, .21, .26])
def plotHist(data):
    #plt.hist([1, 0], bins= [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1], color = 'white')
    #plt.hist(data, bins= [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
    darkRed = [];
    darkBlue = [];
    lightRed = [];
    lightBlue = [];
    for i in data:
      if i > .7:
        darkRed = np.append(darkRed, i)
      elif i > .50:
        lightRed = np.append(lightRed, i)
      elif i > .3:
        lightBlue = np.append(lightBlue, i)
      else:
        darkBlue = np.append(darkBlue, i)
    plt.hist(darkBlue, bins= [0, .1, .2, .3], alpha = .75, color = 'blue', label = 'strongly liberal')
    plt.hist(lightBlue, bins= [.3, .4, .5], alpha = .25, color = 'blue', label = 'mildly liberal')
    plt.hist(lightRed, bins= [.5, .6, .7], alpha = .25, color = 'red', label = 'mildly conservative')
    plt.hist(darkRed, bins= [.7, .8, .9, 1], alpha = .75, color = 'red', label = 'strongly conservative')
    plt.xlabel('political score')
    plt.legend(loc = "upper left")
    max = 0
    totalData = np.array([darkRed, darkBlue, lightRed, lightBlue])
    for x in totalData:
      if len(x) > max:
        max = len(x)
    plt.ylim(0,max*1.25)
    plt.savefig('foo.png')
    return 'foo.png'