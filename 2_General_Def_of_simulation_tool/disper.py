import numpy as np

def dispersion(indata):
    # calculate mean value
    mean = sum(indata)/len(indata)
    print("mean = ",mean)
    # calculate square mean value
    sqmean = sum(np.square(indata))/len(indata)
    print("sqmean = ",sqmean)
    # calculate dispersion
    sigma2 = sqmean - mean
    # calculate standard deviation
    sigma = np.sqrt(sigma2)
    print("sigma = ",sigma)

indata = [1, 1, 4, 1, 1]
outdata = dispersion(indata)
