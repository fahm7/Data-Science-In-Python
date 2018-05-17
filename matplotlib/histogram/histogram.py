
import matplotlib.pyplot as plt


blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
#plt.hist(blood_sugar, rwidth=0.8) # by default number of bins is set to 10

plt.hist(blood_sugar,rwidth=0.5,bins=4)

plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")
plt.show()

#plt.hist(blood_sugar,rwidth=0.5,bins=4)