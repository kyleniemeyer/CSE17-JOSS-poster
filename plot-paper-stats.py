import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.serif'] = ['Open Sans']

months = np.genfromtxt('JOSS-accepted-papers.csv', delimiter=',', usecols=0, dtype=str)
submitted = np.genfromtxt('JOSS-accepted-papers.csv', delimiter=',', usecols=1, dtype=int)
accepted = np.genfromtxt('JOSS-accepted-papers.csv', delimiter=',', usecols=2, dtype=int)


months = [m[0:3] for m in months]

N = len(months)
ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars

# plot accepted
fig, ax = plt.subplots()
rects1 = ax.bar(ind, submitted, width, color='b')

ax.set_ylabel('Number of submitted papers')
ax.set_xticks(ind)
ax.set_xticklabels(months)

fig.tight_layout()
plt.show()
pp = PdfPages('JOSS-submitted-papers.pdf')
pp.savefig()
pp.close()

plt.close()

# plot accepted
fig, ax = plt.subplots()
rects1 = ax.bar(ind, accepted, width, color='g')

ax.set_ylabel('Number of accepted papers')
ax.set_xticks(ind)
ax.set_xticklabels(months)

fig.tight_layout()
plt.show()
pp = PdfPages('JOSS-accepted-papers.pdf')
pp.savefig()
pp.close()
