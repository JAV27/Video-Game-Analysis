import itertools
import statistics 
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Problem 1
data = list(range(1,6))

combs = itertools.combinations(data, 2)
means = []
for comb in combs:
    means.append(statistics.mean(comb))

meansCounter = Counter(means)
keys = meansCounter.keys()
values = meansCounter.values()

# Part a: This is the distribution
plt.bar(keys, values, width=.3)
plt.show()

# Part b:
npmeans = np.array(means)
expectedValue = np.mean(npmeans)
print(expectedValue)

standardDeviation = np.std(means)
print(standardDeviation)

# Note: Not really sure about this one/ E(xbar) = mean so what am I supposed to do?
# Part c:
sampleMean = np.sum(npmeans)/len(npmeans)
print(sampleMean)

sampleStandardDeviation = 1/(np.sqrt(2)) * standardDeviation * np.sqrt(3)/np.sqrt(4)
print(sampleStandardDeviation)

# Problem 2

data = np.array([1,2,2,4,4])
combs = itertools.combinations(data, 3)

medians = []
for comb in combs:
    medians.append(np.median(comb))
print(medians)

mediansCounter = Counter(medians)
keys = mediansCounter.keys()
values = mediansCounter.values()

# Part a: This is the distribution
plt.bar(keys, values, width=.3)
plt.show()

# Part b:
expectedValue = np.mean(medians)
print(expectedValue)

standardDeviation = np.std(medians)
print(standardDeviation)