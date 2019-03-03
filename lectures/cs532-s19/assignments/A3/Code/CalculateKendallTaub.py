from numpy.random import rand
from numpy.random import seed
from scipy.stats import kendalltau
import csv
seed(1)

data1, data2 = [],[]
with open("C:\InputForKendallTau_b1.csv") as inputForKendallTau_b:
    reader_inputForKendallTau_b = csv.reader(inputForKendallTau_b, delimiter=',')
    next(reader_inputForKendallTau_b)
    for row in reader_inputForKendallTau_b:
        #print(row[1])
        data1.append(row[2])
        data2.append(row[3])

coef, p = kendalltau(data1, data2)
print('Kendall correlation coefficient: %.3f' % coef)
alpha = 0.05
if p > alpha:
    print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
    print('Samples are correlated (reject H0) p=%.3f' % p)