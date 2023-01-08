from math import sqrt
from statistics import NormalDist


def z_test(s_mean,p_mean,sd):
    return round(((s_mean - p_mean)*sqrt(n))/sd)

def critical_determiner(zscore,tail):
    if tail == 2:
        crit = NormalDist().inv_cdf((1 + zscore) / 2)
    else:
        crit = NormalDist().inv_cdf(zscore)
    return crit

def hypothesis_test(crit,zscore,tail):
    if tail == 1:
        
