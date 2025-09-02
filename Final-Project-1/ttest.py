import scipy.stats as stats
import numpy as np 
import pandas as pd 

def ttest(x,y):
    cor = x.corr(y)
    df = len(x)-2
    t = cor*np.sqrt(df)
    t = t/np.sqrt(1-cor*cor)
    t = abs(t)
    pval = stats.t.sf(t,df)*2
    
    return pval
