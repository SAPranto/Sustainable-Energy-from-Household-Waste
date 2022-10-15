import sys
import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import predict
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


# Create your views here.
def index(request):
    return render(request, 'index.html');

def insert(request):
    print("form is submitted")
    Temperature = request.POST['Temperature']
    Humidity = request.POST['Humidity']
    
    
    pima = pd.read_csv("assets/csv/file.csv")
    y = pima.Gas
    s = pd.read_csv("assets/csv/file.csv")
    feature_cols = ['Temperature','Humidity']
    X = s[feature_cols] # Features
    X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.3, random_state=1) # 70% training and 30% test
    clf = DecisionTreeClassifier()

    clf = clf.fit(X_train,y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    pred = clf.predict([[Temperature,Humidity]])
    
    
    Gas = pred
    
    insert_Details = predict(Temperature=Temperature,
                                                  Humidity=Humidity,
                                                  Gas = Gas)
    insert_Details.save()
    return render(request, 'index.html')
