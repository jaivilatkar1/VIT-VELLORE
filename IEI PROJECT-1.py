# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:24:27 2021

@author: Jai
"""
#Importing modules
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
#Loading iris dataset
iris=load_iris()
iris1=sns.load_dataset("iris")
#Converting iris dataset to pandas Dataframe
df=pd.DataFrame(iris.data,columns=(iris.feature_names))
print(df.head())    #Printing Dataframe
df['Target']=iris.target
targets=iris.target_names
print(targets)
#Training columns of Dataframe of iris dataset
y_train=df["Target"]
x_train=df.drop("Target",axis=1)
cls=SVC()
print(cls.fit(x_train,y_train))
x_predict=[5.1,3.2,1.5,0.5]
y_predict=cls.predict([x_predict])
print("Targets=",targets[y_predict])
#Calculating sum,mean and median of columos of iris dataset
slsum1=df["sepal length (cm)"].sum()
slmean1=df["sepal length (cm)"].mean()
slmedian1=df["sepal length (cm)"].median()
slsum2=df["sepal width (cm)"].sum()
slmean2=df["sepal width (cm)"].mean()
slmedian2=df["sepal width (cm)"].median()
slsum3=df["petal length (cm)"].sum()
slmean3=df["petal length (cm)"].mean()
slmedian3=df["petal length (cm)"].median()
slsum4=df["petal width (cm)"].sum()
slmean4=df["petal width (cm)"].mean()
slmedian4=df["petal width (cm)"].median()
print("mean:",slmean1,"\t",slmean2,"\t",slmean3,"\t",slmean4)
print("\nmedian:",slmedian1,"\t",slmedian2,"\t",slmedian3,"\t",slmedian4)
print("\nsum:",slsum1,"\t",slsum2,"\t",slsum3,"\t",slsum4)
#Plotting graph for sepal length and sepal width
x1=df["sepal length (cm)"]
y1=df["sepal width (cm)"]
plt.scatter(x1, y1, c ="orange")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.show()
#Plotting graph for petal length and petal width
x2=df["petal length (cm)"]
y2=df["petal width (cm)"]
plt.scatter(x2, y2, c ="green")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.show()
#Plotting using heatmap function of seaborn module
sns.heatmap(iris1.corr(), linecolor = 'white', linewidths = 1)
plt.show()
#Plotting using violinplot function of seaborn module
sns.violinplot(x="petal width (cm)", y="petal length (cm)", data=x_train, size=5, palette = 'colorblind')
plt.show()
#Using KNearestNeighbours function to determine accuracy of data
knn = KNeighborsClassifier(n_neighbors = 6, p = 1, metric='manhattan')
knn.fit(x_train, y_train)
print('The accuracy of the Knn classifier on train data is {:.2f}'.format(knn.score(x_train, y_train)))