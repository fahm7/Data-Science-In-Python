import matplotlib.pyplot as plt

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5,explode=[0,0,0,0.1,0.2])
plt.show()


#Ex2

#plt.axis("equal")
#plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5,explode=[0,0,0,0.1,0.2],counterclock=True, startangle=45)
#plt.show()