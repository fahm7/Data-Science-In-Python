#SCATTER PLOT
# install matplotlib
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
import matplotlib.pyplot as plt


days=[1,2,3,4,5,6,7]
temp=[50,51,52,48,47,49,46]

#STYLE1 : doted lines
#plt.plot(days,temp,color='green', linewidth=5,linestyle='dotted')

plt.title('Weather')
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.plot(days,temp)
#STYLE 2
#plt.plot(days,temp,'b+--')

##STYLE 3

#plt.plot(days,temp,color='blue',marker='+',linestyle='',markersize=20)

#STYLE 4
plt.plot(days,temp,'g<',alpha=0.5) # alpha can be specified on a scale 0 to 1
plt.show()

