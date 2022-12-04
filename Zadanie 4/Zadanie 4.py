import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("zoo.data",
                        names=["Animal_Name", "Hair", "Feathers", "Eggs", "Milk", "Airbone", "Aquatic", "Predator",
                               "Toothed", "Backbone", "Breathes", "Venomous", "Fins", "Legs", "Tail", "Domestic",
                               "Catsize", "Type"])

plt.pie(dataFrame.groupby(['Feathers']).size(), autopct='%1.1f%%', labels=["Don't Have feathers", "Have feathers"])
plt.title("Feathers")
plt.show()

plt.pie(dataFrame.groupby(['Eggs']).size(), autopct='%1.1f%%', labels=["Don't lay eggs", "Lay Eggs"])
plt.title("Lay Eggs")
plt.show()

plt.pie(dataFrame.groupby(['Airbone']).size(), autopct='%1.1f%%', labels=["Don't Fly", "Fly"])
plt.title("Fly")
plt.show()

plt.pie(dataFrame.groupby(['Predator']).size(), autopct='%1.1f%%', labels=["Aren't Predators", "Are predators"])
plt.title("Predator")
plt.show()

plt.pie(dataFrame.groupby(['Venomous']).size(), autopct='%1.1f%%', labels=["Aren't Venomous", "Are Venomous"])
plt.title("Venomous")
plt.show()

plt.pie(dataFrame.groupby(['Tail']).size(), autopct='%1.1f%%', labels=["Don't have tail", "Have Tail"])
plt.title("Tail")
plt.show()


