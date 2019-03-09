import matplotlib
import matplotlib.pyplot as plt
import csv
from sklearn import linear_model
import seaborn as sns
import numpy as np
from statistics import *
from adjustText import adjust_text

friedsCounter = 0
datax, datay = [],[]

with open("C:\\acnwala_twitter_follows_count.csv") as acnwalafriends:
    reader_acnwalafriends = csv.reader(acnwalafriends, delimiter=',')
    next(reader_acnwalafriends)
    for row in reader_acnwalafriends:
        friedsCounter = friedsCounter + 1
        datax.append("f" + str(friedsCounter))
        datay.append(int(row[1]))


datay.sort()
print("Mean :" + str(mean(datay)))
print("Median :" + str(median(datay)))
print("Standard Deviation :" + str(stdev(datay)))
ax = plt.axes()
ax.plot(datax, datay,'.-')
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.annotate('Standard Deviation', xy=(83,2620.146952509964),xytext=(83, 10000),arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Mean', xy=(80,1198.5054945054944),xytext=(80, 12500),arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Median', xy=(47,450),xytext=(47, 2500),arrowprops=dict(facecolor='black', shrink=0.05))