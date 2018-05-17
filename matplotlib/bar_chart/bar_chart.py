import matplotlib.pyplot as plt
import numpy as np

company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]

xpos = np.arange(len(company))
#Example 1
#plt.bar(xpos,revenue, label="Revenue")

plt.xticks(xpos,company)
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()

profit=[40,2,34,12]
plt.bar(xpos-0.2,revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2,profit, width=0.4,label="Profit")

plt.xticks(xpos,company)

plt.show()