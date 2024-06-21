import numpy as np
import statistics as st

def mean(x):
    outputmean = np.mean(x)
    print("The Mean Value of this List is: ", outputmean)     
       

def median(x):
    outputmedian = np.median(x)
    print("The Median Value of the List is: ", outputmedian)

def mode(x):
    nparray = np.array(x)
    outputmode = st.mode(nparray)
    print("The Mode of the List is: ", outputmode)






