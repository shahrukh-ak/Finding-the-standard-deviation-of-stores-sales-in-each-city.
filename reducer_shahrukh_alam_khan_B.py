#!/usr/bin/python
import sys
import math

def update(existingAggregate, newValue):
    (count, mean, M2) = existingAggregate
    count += 1 
    delta = newValue - mean
    mean += delta / count
    delta2 = newValue - mean
    M2 += delta * delta2

    return (count, mean, M2)

def finalize(existingAggregate):
    (count, mean, M2) = existingAggregate
    (mean, variance, sampleVariance) = (mean, M2/count, M2/(count - 1)) 
    if count < 2:
        return float('nan')
    else:
        return (mean, variance, sampleVariance)

S=[0,0,0]

(last_key,value) = (None, 0.0)
for lines in sys.stdin:
    (key,new_value) = lines.split('\t')
    if last_key and key!= last_key:
        
        (average,P_Variance,S_Variance)=finalize(S)
        S_Deviation=math.sqrt(P_Variance)

        print('%s\t%0.2f'%(last_key,S_Deviation))
        (last_key,value) = (key, float(new_value))
        S=[0,0,0]
        S=update(S,value)
    else:
        (last_key,value) = (key, float(new_value))
        S=update(S,value)

if last_key:
    (average,P_Variance,S_Variance)=finalize(S)
    S_Deviation=math.sqrt(P_Variance)
    print('%s\t%0.2f' % (last_key,S_Deviation))
