
# install matplotlib
import matplotlib.pyplot as plt


plt.plot([1,2,3],[5,7,4],linestyle='dashed')


days=[1,2,3,4,5,6,7]
temperature=[50,51,52,48,47,49,46]

plt.plot(days,temperature,color='green', linewidth=5,linestyle='dotted')
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

#https://matplotlib.org/tutorials/index.html

