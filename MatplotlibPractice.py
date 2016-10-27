import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.subplot(331)
plt.plot([1,2,3,4])
plt.ylabel("some numbers")
plt.show()

plt.subplot(332)
plt.plot([2,4,5,6], [1,4,8,16], 'ro')
plt.axis([0, 7, 0, 20])
plt.show()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
print t
 
# red dashes, blue squares and green triangles
plt.subplot(333)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# plt.figure(1)                # the first figure
# plt.subplot(211)             # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)             # the second subplot in the first figure
# plt.plot([4, 5, 6])
# 
# 
# plt.figure(2)                # a second figure
# plt.plot([4, 5, 6])          # creates a subplot(111) by default
# 
# plt.figure(1)                # figure 1 current; subplot(212) still current
# plt.subplot(211)             # make subplot(211) in figure1 current
# plt.title('Easy as 1, 2, 3') # subplot 211 title
# plt.show()

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
 
# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
 
plt.subplot(334) 
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
plt.subplot(335)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()