import pandas as pd
import matplotlib.pyplot as plt


# Zadanie 3
Dataframe = pd.read_csv('iris.data', names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"])
plt.scatter(Dataframe['Sepal Length'].where(Dataframe["Class"]=="Iris-virginica"),Dataframe['Sepal Width'].where(Dataframe["Class"]=="Iris-virginica"),color="red")
plt.scatter(Dataframe['Sepal Length'].where(Dataframe["Class"]=="Iris-versicolor"),Dataframe['Sepal Width'].where(Dataframe["Class"]=="Iris-versicolor"),color="green")
plt.scatter(Dataframe['Sepal Length'].where(Dataframe["Class"]=="Iris-setosa"),Dataframe['Sepal Width'].where(Dataframe["Class"]=="Iris-setosa"),color="blue")
plt.legend(['Iris-virginica',"Iris-versicolor","Iris-setosa"])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()


plt.scatter(Dataframe['Petal Length'].where(Dataframe["Class"]=="Iris-virginica"),Dataframe['Petal Width'].where(Dataframe["Class"]=="Iris-virginica"),color="red")
plt.scatter(Dataframe['Petal Length'].where(Dataframe["Class"]=="Iris-versicolor"),Dataframe['Petal Width'].where(Dataframe["Class"]=="Iris-versicolor"),color="green")
plt.scatter(Dataframe['Petal Length'].where(Dataframe["Class"]=="Iris-setosa"),Dataframe['Petal Width'].where(Dataframe["Class"]=="Iris-setosa"),color="blue")
plt.legend(['Iris-virginica',"Iris-versicolor","Iris-setosa"])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()


plt.scatter(Dataframe['Sepal Length'].where(Dataframe["Class"]=="Iris-virginica"),Dataframe['Petal Width'].where(Dataframe["Class"]=="Iris-virginica"),color="red")
plt.scatter(Dataframe['Sepal Length'].where(Dataframe["Class"]=="Iris-versicolor"),Dataframe['Petal Width'].where(Dataframe["Class"]=="Iris-versicolor"),color="green")
plt.scatter(Dataframe['Sepal Length'].where(Dataframe["Class"]=="Iris-setosa"),Dataframe['Petal Width'].where(Dataframe["Class"]=="Iris-setosa"),color="blue")
plt.legend(['Iris-virginica',"Iris-versicolor","Iris-setosa"])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.show()


plt.scatter(Dataframe['Petal Length'].where(Dataframe["Class"]=="Iris-virginica"),Dataframe['Sepal Width'].where(Dataframe["Class"]=="Iris-virginica"),color="red")
plt.scatter(Dataframe['Petal Length'].where(Dataframe["Class"]=="Iris-versicolor"),Dataframe['Sepal Width'].where(Dataframe["Class"]=="Iris-versicolor"),color="green")
plt.scatter(Dataframe['Petal Length'].where(Dataframe["Class"]=="Iris-setosa"),Dataframe['Sepal Width'].where(Dataframe["Class"]=="Iris-setosa"),color="blue")
plt.legend(['Iris-virginica',"Iris-versicolor","Iris-setosa"])
plt.xlabel("Petal Length")
plt.ylabel("Sepal Width")
plt.show()