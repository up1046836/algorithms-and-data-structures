import os.path
import matplotlib.pyplot as plt
import os.path

with open(os.path.dirname(__file__) + '/../results/running_times.results', 'r') as f:
    data = []
    for line in f:
        data.append(line.split())

    data.pop(0)
    data.pop(0)

headers = ['Naive', 'Hash Table']
    
x = [int(data[i][0]) for i in range(len(data))]

running_times = []
for i in range(1, 5):
    tmp = []
    for n in range(len(x)):
        try:
            tmp.append(float(data[n][i]))
        except:
            tmp.append(None)
    running_times.append(tmp)

plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.xlabel('n')
plt.ylabel('time [seconds]')

for i in range(2):
    plt.plot(x, running_times[i], label=headers[i])

plt.legend()
plt.savefig(os.path.dirname(__file__) + '/../results/graph.png', dpi=1200)
plt.show()
