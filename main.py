import matplotlib.pyplot as plt

values = [9, 15, 11]

for x in values:
    val = [x]
    enum = [1]

    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
        val.append(x)
        enum.append(enum[-1] + 1)

    plt.plot(enum, val,marker='o',markersize=4, label=f'Starting Value: {val[0]}')


plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Collatz Conjecture Sequences')
plt.legend()
plt.grid(True)
plt.show()