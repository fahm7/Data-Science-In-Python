import matplotlib.pyplot as plt

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
#plt.pie(exp_vals,labels=exp_labels)
plt.pie(exp_vals,labels=exp_labels, shadow=True)
plt.axis("equal")


plt.show()