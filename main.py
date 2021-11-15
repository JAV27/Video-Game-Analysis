import itertools
import statistics 
from collections import Counter
import matplotlib.pyplot as plt

# Problem 1
data = list(range(1,6))

combs = itertools.combinations(data, 2)
means = []
for comb in combs:
    means.append(statistics.mean(comb))

means = Counter(means)
keys = means.keys()
values = means.values()

plt.bar(keys, values, width=.3)
plt.show()