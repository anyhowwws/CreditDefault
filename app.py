#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:59:06 2022

@author: hows
"""
from flask import Flask, request, render_template

app = Flask(__name__)

import joblib
from joblib import load

# model = joblib.load("/Users/hows/Documents/CART.joblib")
# pred = model.predict([[20,1]])

# model2 = joblib.load("/Users/hows/Documents/RandomForest.joblib")
# pred2 = model2.predict([[20,1]])

# model3 = joblib.load("/Users/hows/Documents/GB.joblib")
# pred3 = model3.predict([[20,1]])

def prediction(predValue):
    if predValue<0.5:
        return "Nah. Will NOT default =)"
    else:
        return "Yeah! Will default =("
    
def UITranslate(UIoption):
    if UIoption=="yes":
        return 1
    else:
        return 0
    
@app.route("/", methods=["GET","POST"])
def index():
    if request.method =="POST":
        Income=request.form.get("Income")
        #Card=request.form.get("Supplementary card")
        Age=request.form.get("Age")
        Loan=request.form.get("Loan")
        # card = UITranslate(Card)
        # purchase = float(Purchase)
        #card = int(Card)
        income = float(Income)
        age = float(Age)
        loan = float(Loan)
        
        model1 = load("CART")
        model2 = load("RandomForest")
        model3 = load("GB")
        
        pred1 = model1.predict([[income,age,loan]])
        pred2 = model2.predict([[income,age,loan]])
        pred3 = model3.predict([[income,age,loan]])
            
        Result1="CART says: "+prediction(pred1[0])
        Result2="Random Forest says: "+prediction(pred2[0])
        Result3="XGBoost says: "+prediction(pred3[0])

        # return(render_template("/Users/hows/Documents/week2/templates/index.html",result="1",result2="2",result3="3"))
        return(render_template("index.html",result=Result1,result2=Result2,result3=Result3))
        #return(render_template("index.html",result="1",result2="2",result3="3"))
            
    else:
        # defaultRate=""
        # defaultResults = ""
        # defaultResponse = "Enter an amount above for an estimation!"
        # return(render_template("/Users/hows/Documents/week2/templates/index.html",result="1",result2="2",result3="3"))
        return(render_template("index.html",result="Enter your values above to start!",result2="",result3=""))


if __name__=="__main__": #required if not in DEV env
    # app.run(host="127.0.0.1",port=int("1415"))
    app.run()
